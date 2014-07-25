# Copyright 2013 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implements all necessary Impala HiveServer 1 RPC functionality."""

# This work builds off of:
# 1. the Hue interface:
#       hue/apps/beeswax/src/beeswax/server/dbms.py
#       hue/apps/beeswax/src/beeswax/server/hive_server2_lib.py
#       hue/desktop/core/src/desktop/lib/thrift_util.py
# 2. the Impala shell:
#       Impala/shell/impala_shell.py

import datetime
import socket
import operator
import exceptions
import re

from decimal import Decimal

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport, TTransportException
from thrift.protocol.TBinaryProtocol import TBinaryProtocol, TBinaryProtocolAccelerated

from beeswaxd import BeeswaxService
from beeswaxd.BeeswaxService import QueryState
from ImpalaService import ImpalaService
from ImpalaService.ImpalaService import TImpalaQueryOptions, TResetTableReq
from ImpalaService.ImpalaService import TPingImpalaServiceResp
from Status.ttypes import TStatus, TStatusCode

# datetime only supports 6 digits of microseconds but Impala supports 9.
# If present, the trailing 3 digits will be ignored without warning.
_TIMESTAMP_PATTERN = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+(\.\d{,6})?)')

TYPE_MAP = {
    'int': int,
    'bigint': long,
    'float': float
}

def _parse_timestamp(value):
    if value:
        match = _TIMESTAMP_PATTERN.match(value)
        if match:
            if match.group(2):
                format = '%Y-%m-%d %H:%M:%S.%f'
                # use the pattern to truncate the value
                value = match.group()
            else:
                format = '%Y-%m-%d %H:%M:%S'
            value = datetime.datetime.strptime(value, format)
        else:
            raise Exception(
                    'Cannot convert "{}" into a datetime'.format(value))
    else:
        value = None
    return value


def retry(func):
    # Retries RPCs after closing/reopening transport
    # `service` must be the first arg in args or must be a kwarg

    def wrapper(*args, **kwargs):
        # get the thrift transport
        if 'service' in kwargs:
            transport = kwargs['service']._iprot.trans
        elif len(args) > 0 and isinstance(args[0], ImpalaService.Client):
            transport = args[0]._iprot.trans
        else:
            raise HS2Error("RPC function does not have expected 'service' arg")

        tries_left = 3
        while tries_left > 0:
            try:
                if not transport.isOpen():
                    transport.open()
                return func(*args, **kwargs)
            except socket.error as e:
                pass
            except TTransportException as e:
                pass
            except Exception as e:
                raise
            transport.close()
            tries_left -= 1
        raise

    return wrapper

# _get_socket and _get_transport based on the Impala shell impl
def _get_socket(host, port, use_ssl, ca_cert):
    if use_ssl:
        from thrift.transport.TSSLSocket import TSSLSocket
        if ca_cert is None:
            return TSSLSocket(host, port, validate=False)
        else:
            return TSSLSocket(host, port, validate=True, ca_certs=ca_cert)
    else:
        return TSocket(host, port)

def _get_transport(sock, host, use_ldap, ldap_user, ldap_password, use_kerberos,
        kerberos_service_name):
    if not use_ldap and not use_kerberos:
        return TBufferedTransport(sock)
    try:
      import saslwrapper as sasl
    except ImportError:
      import sasl
    from impala.thrift_sasl import TSaslClientTransport
    def sasl_factory():
        sasl_client = sasl.Client()
        sasl_client.setAttr("host", host)
        if use_ldap:
            sasl_client.setAttr("username", ldap_user)
            sasl_client.setAttr("password", ldap_password)
        else:
            sasl_client.setAttr("service", kerberos_service_name)
        sasl_client.init()
        return sasl_client
    if use_kerberos:
        return TSaslClientTransport(sasl_factory, "GSSAPI", sock)
    else:
        return TSaslClientTransport(sasl_factory, "PLAIN", sock)

def connect_to_impala(host, port=21000, timeout=45, use_ssl=False, ca_cert=None,
        use_ldap=False, ldap_user=None, ldap_password=None, use_kerberos=False,
        kerberos_service_name='impala'):
    sock = _get_socket(host, port, use_ssl, ca_cert)
    sock.setTimeout(timeout * 1000.)
    transport = _get_transport(sock, host, use_ldap, ldap_user, ldap_password,
                               use_kerberos, kerberos_service_name)
    transport.open()
    protocol = TBinaryProtocolAccelerated(transport)
    service = ImpalaService.Client(protocol)
    return service

def close_service(service):
    service._iprot.trans.close()

def reconnect(service):
    service._iprot.trans.close()
    service._iprot.trans.open()

def create_beeswax_query(query_str, user):
    """Create a beeswax query object from a query string"""
    query = BeeswaxService.Query()
    query.hadoop_user = user
    query.query = query_str
    query.configuration = []
    return query

@retry
def execute_statement(service, statement, user):
    query = create_beeswax_query(statement, user=user)
    query_handle = service.query(query)
    return query_handle

@retry
def get_result_schema(service, query_handle):
    metadata = service.get_results_metadata(query_handle)
    #metadata, _ = service.fetch(query_handle, False, 10)
    schema = [(fs.name, fs.type) for fs in metadata.schema.fieldSchemas]

    return schema

@retry
def fetch_results(service, query_handle, schema=None, max_rows=100):

    # the schema is necessary to pull the proper values (i.e., coalesce)
    if schema is None:
        schema = get_result_schema(service, query_handle)

    response = service.fetch(query_handle, False, max_rows)
    rows = []
    types = [TYPE_MAP.get(row[1]) for row in schema]
    for trow in response.data:
        row_data = trow.split('\t')
        row = []
        for (i, col_val) in enumerate(row_data):
            type_ = schema[i][1]
            #type_converter = TYPE_MAP.get(type_, unicode)
            #value = type_converter(col_val)
            value = col_val
            
            #if type_ == 'TIMESTAMP_TYPE':
            #    value = _parse_timestamp(value)
            #elif type_ == 'DECIMAL_TYPE':
            #    if value: value = Decimal(value)
            row.append(value)
        rows.append(tuple(row))

    return rows

@retry
def get_current_database(service, session_handle):
    raise NotImplementedError

@retry
def get_databases(service, user):
    databases_query = execute_statement(service, "SHOW DATABASES", user)
    rows = fetch_results(service, databases_query, max_rows=1024)
    databases = []
    for row in rows:
        databases.append(row[0])
    return databases

@retry
def database_exists(service, session_handle, db_name):
    req = TGetSchemasReq(sessionHandle=session_handle, schemaName=db_name)
    resp = service.GetSchemas(req)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row ideally
    results = fetch_results(service=service, operation_handle=operation_handle)
    exists = False
    for result in results:
        if result[0] == db_name:
            exists = True
    close_operation(service, operation_handle)
    return exists

@retry
def get_tables(service, session_handle, database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle,
                        schemaName=database_name,
                        tableName='.*')
    resp = service.GetTables(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle

@retry
def table_exists(service, session_handle, table_name, database_name='.*'):
    req = TGetTablesReq(sessionHandle=session_handle,
                        schemaName=database_name,
                        tableName=table_name)
    resp = service.GetTables(req)
    err_if_rpc_not_ok(resp)
    operation_handle = resp.operationHandle
    # this only fetches default max_rows, but there should only be one row ideally
    results = fetch_results(service=service, operation_handle=operation_handle)
    exists = False
    for result in results:
        if result[2] == table_name:
            exists = True
    close_operation(service, operation_handle)
    return exists

@retry
def get_table_schema(service, session_handle, table_name, database_name='.*'):
    req = TGetColumnsReq(sessionHandle=session_handle,
                         schemaName=database_name,
                         tableName=table_name,
                         columnName='.*')
    resp = service.GetColumns(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle

@retry
def get_functions(service, session_handle, database_name='.*'):
    # TODO: need to test this one especially
    req = TGetFunctionsReq(sessionHandle=session_handle,
                           schemaName=database_name,
                           functionName='.*')
    resp = service.GetFunctions(req)
    err_if_rpc_not_ok(resp)
    return resp.operationHandle

@retry
def get_operation_status(service, operation_handle):
    req = TGetOperationStatusReq(operationHandle=operation_handle)
    resp = service.GetOperationStatus(req)
    err_if_rpc_not_ok(resp)
    return TOperationState._VALUES_TO_NAMES[resp.operationState]

@retry
def cancel_operation(service, operation_handle):
    req = TCancelOperationReq(operationHandle=operation_handle)
    resp = service.CancelOperation(req)
    err_if_rpc_not_ok(resp)

@retry
def close_operation(service, operation_handle):
    req = TCloseOperationReq(operationHandle=operation_handle)
    resp = service.CloseOperation(req)
    err_if_rpc_not_ok(resp)

@retry
def get_log(service, operation_handle):
    req = TGetLogReq(operationHandle=operation_handle)
    resp = service.GetLog(req)
    err_if_rpc_not_ok(resp)
    return resp.log

def ping(service, session_handle):
    req = TGetInfoReq(sessionHandle=session_handle,
                      infoType=TGetInfoType.CLI_SERVER_NAME)
    try:
        resp = service.GetInfo(req)
    except TTransportException as e:
        return False

    try:
        err_if_rpc_not_ok(resp)
    except HS2Error as e:
        return False
    return True
