import re
import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost,11433;"
                      "Database=Hackathon;"
                      "uid=sa;pwd=Lloyds2022!")
print("DB is connected")

cursor = cnxn.cursor()
query = "SELECT * FROM PRODUCTS"
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    print(row)
