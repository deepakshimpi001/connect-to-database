import mysql.connector

conn=mysql.connector.connect(user='root',host="localhost",password="9552207859",database="hr")

print(conn)

cursorobject=conn.cursor()

cursorobject.execute("create database geeksforgeek")