import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB is connected")

cursor = connection.cursor()
cursor.execute('Select * FROM products')
products = cursor.fetchall()
connection.close()

print(products)