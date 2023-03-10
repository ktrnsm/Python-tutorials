
import mysql.connector
baglan=mysql.connector.connect(host="localhost",user="root",password="Sehersebnem1.",database="simple")
db=baglan.cursor()
sorgu=("Create Table Information(id INT(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(25) NOT NULL, Tc VARCHAR(11) NOT NULL, Cinsiyet VARCHAR(5) NOT NULL, Yas INT NOT NULL, Yer VARCHAR(20) NOT NULL")
sorgu2=("INSERT INTO inf(Name)")
db.execute(sorgu)
soq=db.fetchall()
for i in soq:
    print(i)