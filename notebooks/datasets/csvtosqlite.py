import pandas as pd
import feather
import sqlite3

df = pd.read_csv('HR_COM1.CSV')

print("saving the file sqlite3...")

conn = sqlite3.connect('turnover_hr.sqlite')

df.to_sql('employees', conn, if_exists='replace', index=False)

df = pd.read_sql_query("SELECT * from employees", conn)

print(df)

conn.close()