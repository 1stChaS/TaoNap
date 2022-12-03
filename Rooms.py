import json
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
        self.__rooms_name = new_rooms

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, new_floor):
        if not new_floor.isnumeric():
            raise ValueError("Floor should be numeric")
        self.__floor = new_floor

    def search(self):
        check = False
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                if self.floor == "1":
                    if self.__rooms_name == i['name_room']:
                        try:
                            with open("Customers_info.json", "r") as data_file:
                                data = json.load(data_file)
                        except FileNotFoundError:
                            pass
                        else:
                            for k in data.values():
                                if self.rooms_name == k["Room"]:
                                    print("Oh, sorry for the inconvenience but someone have already book this room.")
                                    return False
                        check = True

                if self.__floor == "2":
                    if self.__rooms_name == i['name_room']:
                        try:
                            with open("Customers_info.json", "r") as data_file:
                                data = json.load(data_file)
                        except FileNotFoundError:
                            pass
                        else:
                            for k in data.values():
                                if self.rooms_name == k["Room"]:
                                    print("Oh, sorry for the inconvenience but someone have already book this room.")
                                    return False
                        check = True

            if not check:
                print("Sorry, we don’t have a room that you want to book.")
                return False
            return True

    def price(self):
        with open('Rooms.csv', "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                if i['floor'] == self.floor and i['name_room'] == self.rooms_name:
                    return int(i['price'])
        # ValueError: I/O operation on closed file is meaning for loop not in with open
