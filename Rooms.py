import Taonap_Bill
import csv


class Rooms:
    def __init__(self, rooms_name, floor):
        self.__rooms_name = rooms_name
        self.__floor = floor

    @property
    def rooms_name(self):
        return self.__rooms_name

    @rooms_name.setter
    def rooms_name(self, new_rooms):
        self.rooms_name = new_rooms

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, new_floor):
        self.floor = new_floor

    def check(self):
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                if self.__floor == "1":
                    if i['floor'] == "1" and self.__rooms_name == i['name_room']:
                        check = True

                if self.__floor == "2":
                    if i['floor'] == "2" and self.__rooms_name == i['name_room']:
                        check = True
            if not check:
                print("Sorry, we don’t have a room that you want to book.")
                return False
            return True

    def price(self):
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                if i['floor'] == self.__floor and i['name_room'] == self.__rooms_name:
                    return int(i['price'])
        # ValueError: I/O operation on closed file is meaning for loop not in with open
