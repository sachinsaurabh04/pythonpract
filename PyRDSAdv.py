# Need to install the mysql connector using below command.
# "C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python"

import mysql.connector

#Creating the connection using the mysql connector
mydb = mysql.connector.connect(
  host="mysqldb.cuiqru9uagcw.us-east-1.rds.amazonaws.com",
  user="admin",
  password="admin123"
)

#create an object of the cursor() class
mycursor = mydb.cursor()
mycursor.execute("use test")                  #using a database
mycursor.execute("show tables")               #show tables
for x in mycursor:                            #iterating the table name
    print(x)
mycursor.execute("select * from Persons")     #showing the table Persons content
for y in mycursor:                            #iterating the persons table content
    print(y)
