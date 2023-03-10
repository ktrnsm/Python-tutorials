#119 My SQL setup
import mysql.connector

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sehersebnem1."
    #database="sample"
)
#print(data)

new=data.cursor()
new.execute("CREATE DATABASE sample4")
#new.execute("select*from sample.sales")
#for i in new:
#    print(i)

