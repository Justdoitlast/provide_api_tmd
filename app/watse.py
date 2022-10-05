

import psycopg2
import json
import pandas as pd
def get_db_connection():
    conn = psycopg2.connect(
        host="202.139.197.37",
        database="agridb",
        user="agriuser",
        port="5432",
        password="Agri_2020@gbdi")
    return conn
print(get_db_connection())

conn = get_db_connection()
cursor = conn.cursor()
postgreSQL_select_Query = """select * from "TMD_API".tmd_api limit 1 """

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from mobile table using cursor.fetchall")
tmd = cursor.fetchall()
print(tmd)
colnames = [desc[0] for desc in cursor.description]
print(colnames)
print("-----------------------------------")
j_file = json.dumps([{colname: tmd_data} for colname, tmd_data in zip(colnames, tmd)])
print(j_file)