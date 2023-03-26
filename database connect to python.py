import mysql.connector

conn=mysql.connector.connect(user='root',host="localhost",password="9552207859",database="hr")

#print(conn)

cursorobject=conn.cursor()
try:
    cursorobject.execute("create database geeksforgeek")

except:
    print("database alredy created")