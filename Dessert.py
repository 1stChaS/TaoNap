import csv


class Dessert:
    def __init__(self, menu):
        self.__menu = menu

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu):
        self.menu = new_menu

    def search(self):
        with open("Dessert.csv", "r") as file:
            data_dessert = csv.DictReader(file)
            for i in data_dessert:
                if self.__menu == i['list']:
                    return i['menu']
                check = False
        if not check:
            print("Sorry, we don’t have a dessert that you want.")
            print("Please try again.")

    def price(self):
        with open("Dessert.csv", "r") as file:
            data_dessert = csv.DictReader(file)
            for i in data_dessert:
                if self.__menu == i['list']:
                    return int(i['price'])


