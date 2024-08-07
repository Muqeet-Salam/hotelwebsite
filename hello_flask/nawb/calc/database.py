import mysql.connector

# Establishing the connection to the MySQL server (not a specific database)
mydb = mysql.connector.connect(
    host="localhost",
    user="nawb",
    password="bk201phile",
    database = "roominfo"
)

mycursor = mydb.cursor()

val = (str(3))

mycursor.execute("UPDATE rooms SET available = '0' WHERE room_num = '3'")
mydb.commit()