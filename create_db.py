import duckdb
import pandas as pd

DATABASE='data/eurocup.db'

def get_query(sql_location):
   """read the contents of the sql file"""
   with open(sql_location, 'r') as f:
      _sql = f.read()
    
   return _sql

sql_query_import_1 = get_query('data/sql_query_import_1.sql')
sql_query_import_2 = get_query('data/sql_query_import_2.sql')

with duckdb.connect(DATABASE) as con:
    con.sql(f"{sql_query_import_1}")
    con.sql(f"{sql_query_import_2}")
