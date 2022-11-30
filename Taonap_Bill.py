import sys
import time
sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())


class Customer:
    def __init__(self, customer_name, customer_nickname, customer_phone, room_info, dessert_info, book):
        if not customer_name.isalpha():  # name with surname ex. Chananthida Sopaphol
            raise TypeError("Your name should be string.")
        if not customer_nickname.isalpha():
            raise ValueError("Your nickname should be string.")
        if not customer_phone.isnumeric():
            raise ValueError("Your phone number should be numeric.")
        if len(customer_phone) != 10:
            raise ValueError("Your phone number should have 10 digits.")
        self.__customer_name = customer_name
        self.__customer_nickname = customer_nickname
        self.__customer_phone = customer_phone
        self.__room_info = room_info
        self.dessert_info = dessert_info
        self.__book = book

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, new_name):
        if not new_name.isalpha():
            raise TypeError("Your name should be string.")
        self.__customer_name = new_name

    @property
    def customer_nickname(self):
        return self.__customer_nickname

    @customer_nickname.setter
    def customer_nickname(self, new_nickname):
        if not new_nickname.isalpha():
            raise ValueError("Your nickname should be string.")
        self.__customer_nickname = new_nickname

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, new_phone):
        if not new_phone.isnumeric():
            raise ValueError("Your phone number should be numeric.")
        if len(new_phone) != 10:
            raise ValueError("Your phone number should have 10 digits.")
        self.__customer_phone = new_phone

    @property
    def room_info(self):
        return self.__room_info

    @room_info.setter
    def room_info(self, new_room):
        self.__room_info = new_room

    @property
    def dessert_info(self):
        return self.__dessert_info

    @dessert_info.setter
    def dessert_info(self, new_dessert):
        self.__dessert_info = new_dessert

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, new_book):
        self.__book = new_book

    def print_bill(self):
        total_price = []
        file_name = time.strftime(self.customer_name+"%d-%b-%Y_%H:%M:%S", time.localtime())
        with open(file_name+".txt", "w") as new_bill:
            for i in range(101):
                new_bill.write("=")
            new_bill.writelines("\n" "\n")
            new_bill.write(f"{'TAONAP':^100}\n")
            new_bill.write(f"{'-- No day is so bad it can’t be fixed with a nap --':^100}\n \n")
            for i in range(101):
                new_bill.write("-")
            new_bill.write("\n")
            new_bill.write(f"{'  Menu':<60} {'Quantity':^20}{'Price':^20}\n")
            for i in range(101):
                new_bill.write("-")
            new_bill.write("\n")

            for i in range(len(self.room_info)):
                # Floor: 2, Room: P1
                # room_info.append([floor, select_room, hours, price])
                total_price.append(self.room_info[i][3])
                new_bill.write(f"  Floor: {self.room_info[i][0]}\n")
                new_bill.write(f"  --- Room: {self.room_info[i][1]:<50}"
                               f"{self.room_info[i][2]:^20}{self.room_info[i][3]:^20}\n")

            for k in range(len(self.dessert_info)):
                # dessert_info.append([check, order, price])
                total_price.append(self.dessert_info[k][2])
                new_bill.write(f"  {self.dessert_info[k][0]:<60}"
                               f"{self.dessert_info[k][1]:^20}{self.dessert_info[k][2]:^20}\n")

            for j in range(len(self.book)):
                total_price.append(10)
                new_bill.write(f"  {self.book[j][0]:<60}\n")
                new_bill.write(f"   -- by {self.book[j][1]:<53}{'1':^20}{'10':^20}\n")

            for i in range(101):
                new_bill.write("-")
            new_bill.write("\n")
            new_bill.write(f"  Total price: {sum(total_price)} Baht.\n")
            new_bill.write("\n")
            new_bill.write(f"  Name: {self.customer_name}\n")
            new_bill.write(f"  Nickname: {self.customer_nickname}\n")
            new_bill.write(f"  Phone number: {self.customer_phone}\n")
            for i in range(101):
                new_bill.write("-")
            new_bill.write("\n")
            new_bill.write("\n")
            new_bill.write(f"{'Thank you! Your booking is confirmed.':^100}\n")
            new_bill.write(f"{'Have a good day 😊':^100}\n")
            new_bill.write("\n")
            new_bill.write("\n")
            for i in range(101):
                new_bill.write("=")

