#122 MySQL
import mysql.connector
data=mysql.connector.connect(
    host="localhost",
    user="root",
    pasword="Sehersebnem1."
)
new=data.cursor()
que=("Create Table inf(id INT(5)UNSIGNED AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(15) NOT NULL, Lastname VARCHAR(15)))")
que2="INSERT INTO Hospital.inf(Name,Lastname) VALUES('ktrn','smh')"
new.execute(que)