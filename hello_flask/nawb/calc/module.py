import views

class Room:
        def __init__(self, room_number, floor, num_bedrooms):
            self.room_number = room_number
            self.floor = floor
            self.num_bedrooms = num_bedrooms
            self.is_available = True

        def __str__(self):
            return f"Room {self.room_number} on floor {self.floor} with {self.num_bedrooms} bedrooms"
    
class Guest:
        def __init__(self, name, contact):
            self.name = name
            self.contact = contact

        def __str__(self):
            return f"Guest {self.name}, Contact: {self.contact}"
    
class Reservation:
        def __init__(self, guest, room, check_in_date, check_out_date):
            self.guest = guest
            self.room = room
            self.check_in_date = check_in_date
            self.check_out_date = check_out_date
            self.is_active = True

        def __str__(self):
            return (f"Reservation for {self.guest} in {self.room} "
                    f"from {self.check_in_date} to {self.check_out_date}")
    
class Hotel:
        def __init__(self):
            self.rooms = self._create_rooms()
            self.reservations = []

        def _create_rooms(self):
            rooms = []
            room_number = 1
            for floor in range(1, 5):
                for i in range(1, 5):
                    num_bedrooms = 1 if i <= 2 else 2
                    rooms.append(Room(room_number, floor, num_bedrooms))
                    room_number += 1
            return rooms

        def check_availability(self, num_bedrooms):
            available_rooms = [room for room in self.rooms if room.is_available and room.num_bedrooms == num_bedrooms]
            return available_rooms

        def book_room(self, guest, num_bedrooms, check_in_date, check_out_date):
            available_rooms = self.check_availability(num_bedrooms)
            if not available_rooms:
                return None

            room = available_rooms[0]
            room.is_available = False
            reservation = Reservation(guest, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            return reservation

        def checkout_room(self, reservation):
            reservation.room.is_available = True
            reservation.is_active = False