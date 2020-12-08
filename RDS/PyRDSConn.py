#host =mysqldb.cuiqru9uagcw.us-east-1.rds.amazonaws.com
#user =admin
#password =admin123
#database =test
#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
  host="mysqldb.cuiqru9uagcw.us-east-1.rds.amazonaws.com",
  user="admin",
  password="admin123"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)