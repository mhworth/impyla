#!/usr/bin/env python
import impala.rpc_beeswax as rpc
from impala.dbapi import connect

TEST_QUERY = "SELECT * FROM sometable"
def print_row(row):
    print '\t'.join([str(v) for v in row])

def test_rpc():
    service = rpc.connect_to_impala('localhost')
    query_handle = rpc.execute_statement(service, TEST_QUERY, user='support')
    schema = rpc.get_result_schema(service, query_handle)
    max_rows = 1024
    rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)
    while len(rows) > 0:
        rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)
        map(print_row, rows)
        

    print rpc.get_databases(service, 'support')
    


def test_dbapi():
    connection = connect(port=21000, rpc_impl='hs1')
    cursor = connection.cursor()
    cursor.execute(TEST_QUERY)
    print cursor.fetchall()

test_dbapi()
