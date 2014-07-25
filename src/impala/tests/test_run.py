#!/usr/bin/env python
import impala.rpc_beeswax as rpc

def print_row(row):
    print '\t'.join([str(v) for v in row])
service = rpc.connect_to_impala('localhost')
query_handle = rpc.execute_statement(service, "SELECT * FROM deepfield_drill_small_step300.drill_small_2014_07_14t14_30", user='support')
schema = rpc.get_result_schema(service, query_handle)
max_rows = 1024
rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)
while len(rows) > 0:
    rows = rpc.fetch_results(service, query_handle, schema=schema, max_rows=max_rows)
    map(print_row, rows)
    

print rpc.get_databases(service, 'support')
    


