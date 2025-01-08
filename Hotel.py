class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price
        self.is_room_occupied = False

    def check_if_room_is_empty(self):
        return not self.is_room_occupied

class Guest:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

class Manager:
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_in(self, guest, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.check_if_room_is_empty():
                    room.is_room_occupied = True
                    self.guests.append(guest)
                    print(f"Guest {guest.name} is settled down in room {room_number}")
                    return
                else:
                    print(f"The room {room_number} is already occupied")
                    return
        print(f"Room {room_number} not found.")

    def check_out(self, guest, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_room_occupied:
                    room.is_room_occupied = False
                    self.guests.remove(guest)
                    print(f"The guest {guest.name} has checked out from room {room_number}")
                    return
                else:
                    print(f"Room {room_number} is already empty")
                    return
        print(f"Room {room_number} not found.")

    def information_about_rooms(self):
        for room in self.rooms:
            status = "Occupied" if room.is_room_occupied else "Empty"
            print(f"Room {room.room_number}: {status}")

    def show_guests(self):
        if not self.guests:
            print("No guests currently in the hotel.")
        else:
            for guest in self.guests:
                print(f"Guest: {guest.name}, Passport: {guest.passport_number}")
