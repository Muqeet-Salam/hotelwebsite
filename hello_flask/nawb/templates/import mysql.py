import mysql.connector as sqc

mydb = sqc.connect(
    host="localhost",
    user="nawb",
    password="bk201phile",
    database="demi"
)

def get_doctor_id(hospital_id):
    mycursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM Doctor WHERE Hospital_id = %s"
    mycursor.execute(query, (hospital_id,))
    result = mycursor.fetchall()
    for row in result:
        print("Doctor Name:", row['Doctor_Name'])

get_doctor_id(1)
