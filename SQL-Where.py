import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="examination"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM guardian WHERE guardian_id =4"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)