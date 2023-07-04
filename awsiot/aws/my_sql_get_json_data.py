import mysql.connector
import json

mydb =mysql.connector.connect(host="localhost",user="myuser2",password="mysql",database="mydb2")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM mytable2")

rows = mycursor.fetchall()
data = []
for row in rows:
    data={"Temperature": row[1],"Humidity": row[2],"Version": row[3],"Timestamp": row[4]}
    print(data)
mydb.close()
