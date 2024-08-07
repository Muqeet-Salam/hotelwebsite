import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = 'nawb', password= 'bk201phile', database = 'nawb')
mycursor = mydb.cursor()
mycursor.execute("select * from manga")
result = mycursor.fetchall()
for i in result:
    print(i)