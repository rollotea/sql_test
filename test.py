import mysql.connector as mydb
import pandas as pd
import pandas.io.sql as psql
# コネクションの作成
conn = mydb.connect(
    host='localhost',
    port='3306',
    user='root',
    password='dxftk286',
    database='pets'
)
read_sql = """SELECT * FROM mytable"""
data = psql.read_sql(read_sql, conn)