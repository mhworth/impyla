#!/usr/bin/env python
import impala.rpc_beeswax as rpc

service = rpc.connect_to_impala('localhost')
query_handle = rpc.execute_statement(service, "SELECT * FROM deepfield_drill_small_step300.drill_small_2014_07_14t14_30", user='support')
schema = rpc.get_result_schema(service, query_handle)
max_rows = 1024
rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)
while len(rows) > 0:
    print len(rows)
    rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)

print rpc.get_databases(service, 'support')
    


