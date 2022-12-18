import json
import csv


class Rooms:
    def __init__(self, rooms_name, floor):
        # Input a room's name and its floor that customer wants.
        self.__rooms_name = rooms_name
        self.__floor = floor

    @property
    def rooms_name(self):
        return self.__rooms_name

    @rooms_name.setter
    def rooms_name(self, new_rooms):
        self.__rooms_name = new_rooms

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, new_floor):
        self.__floor = new_floor

    def search(self):
        check = False
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for i in csv_reader:
                check = False
                # Search room's name lists from Rooms.csv.
                if self.floor == "1":
                    if self.rooms_name == i['name_room'] and self.floor == "1":
                        try:
                            with open("Customers_info.json", "r") as data_file:
                                data = json.load(data_file)
                        except FileNotFoundError:
                            pass
                        else:
                            # Check Booking status.
                            for k in data.values():
                                if self.rooms_name == k["Room"]:
                                    # If the room has already booked.
                                    print("Oh, sorry for the inconvenience but someone have already book this room.")
                                    return False
                        check = True

                if self.floor == "2":
                    if self.rooms_name == i['name_room'] and self.floor == "2":
                        try:
                            with open("Customers_info.json", "r") as data_file:
                                data = json.load(data_file)
                        except FileNotFoundError:
                            pass
                        else:
                            # Check Booking status.
                            for k in data.values():
                                if self.rooms_name == k["Room"]:
                                    # If the room has already booked.
                                    print("Oh, sorry for the inconvenience but someone have already book this room.")
                                    return False
                        check = True

            if not check:
                # The room is not in Rooms.csv.
                print("Sorry, we don’t have a room that you want to book.")
                print("Please try again")
                return False
            return True

    def price(self):
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                # Search the room's price from Rooms.csv.
                if i['floor'] == self.floor and i['name_room'] == self.rooms_name:
                    return int(i['price'])
