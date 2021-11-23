#SELECT 

import mysql.connector

mydatabase = mysql.connector.connect(
  host="localhost",
  username="root",
  password="",
  database = "examination"
)

myconn = mydatabase.cursor()   #creates session for executing sql commands

myconn.execute("SELECT *FROM guardian;")
myresult = myconn.fetchall()

for x in myresult:
  print(x)