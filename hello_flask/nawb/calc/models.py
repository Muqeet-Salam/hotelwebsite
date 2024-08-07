import mysql.connector
from datetime import datetime

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="nawb",
    password="bk201phile",
    database="roominfo"
)

class Reservation:
    def __init__(self, name, contact, num_rooms, indate, outdate, room_number):
        self.name = name
        self.contact = contact
        self.num_rooms = num_rooms
        self.indate = indate
        self.outdate = outdate
        self.room_number = room_number
        self.create_reservation()

    def create_reservation(self):
        mycursor = mydb.cursor()
        try:
            mycursor.execute("UPDATE rooms SET available = '0' WHERE room_num = %s", (self.room_number,))
            mydb.commit()
            sql = "INSERT INTO reservation (name, contact, room_number, indate, outdate) VALUES (%s, %s, %s, %s, %s)"
            val = (self.name, self.contact, self.room_number, self.indate, self.outdate)
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()

class Hotel:
    def book_room(self, name, contact, num_rooms, indate, outdate):
        mycursor = mydb.cursor()
       
        mycursor.execute("SELECT room_num FROM rooms WHERE num_room = %s AND available = '1' LIMIT 1", (num_rooms,))
        result = mycursor.fetchone()
            
        
        room_number = result[0]
        mycursor.execute("SELECT floor_num FROM rooms WHERE room_num = %s", (room_number,))
        result2 = mycursor.fetchone()
        floor_num = result2[0]
        final_result = [room_number[0], floor_num[0]]
        reservation = Reservation(name, contact, num_rooms, indate, outdate, room_number[0])
        return final_result
        
           
        

    def checkout(self, name, contact, room_number):
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT room_number FROM reservation WHERE contact = %s AND name = %s", (contact, name))
        result = mycursor.fetchall()
        roomlist = []
        for i in result:
            roomlist.append(i[0])
        for i in roomlist:
            if str(i) == str(room_number):
                sql = "UPDATE rooms SET available = '1' WHERE room_num = %s"
                val = (room_number,)
                mycursor.execute(sql,val)
                mydb.commit()
                return True