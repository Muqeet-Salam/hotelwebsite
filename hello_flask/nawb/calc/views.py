from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import mysql.connector
hotel = Hotel()
mydb = mysql.connector.connect(
    host="localhost",
    user="nawb",
    password="bk201phile",
    database = "roominfo"
)
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'User'} ); 

def final(request):
    name = request.POST['name']
    contact = request.POST['contact']
    rooms = request.POST['rooms']
    indate = request.POST['indate']
    outdate = request.POST['outdate']
    obj = hotel.book_room(name,contact,rooms,indate,outdate)

    if obj:
        return render(request, 'final.html', {'result': obj})
    

def availableroom(request):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM rooms WHERE available = '1'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    context = {
        'rooms': result
    }
    
    return render(request, 'availableroom.html', context)

def bookroom(request):
    return render(request, 'home.html')
def checkout(request):
    return render(request, 'checkout.html')
def checkedout(request):
    name = request.POST['name']
    contact = request.POST['contact']
    room_number = request.POST['rooms']
    obj = hotel.checkout(name,contact,room_number)
    if obj:
        return render(request, 'finalcheckout.html')
    

