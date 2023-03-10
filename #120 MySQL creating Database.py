#120 MySQL creating Database
import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sehersebnem1."
)

print(database)
