import csv
import json


class Books:
    def __init__(self, order):
        # Input an order that customer wants.
        self.__order = order

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, new_order):
        self.__order = new_order

    def search(self):
        with open("Books.csv", "r") as file:
            data_books = csv.DictReader(file)
            book_info = []

            for i in data_books:
                # Search book lists from Books.csv.
                if self.order == i['order']:
                    try:
                        with open("Customers_info.json", "r") as data_file:
                            data = json.load(data_file)
                    except FileNotFoundError:
                        pass
                    else:
                        # Check Booking status.
                        for k in data.values():
                            for m in k["Books"]:
                                if m[0] == i['book_name']:
                                    # If a book has already booked.
                                    print("Oh, sorry for the inconvenience but someone is reading this book right now.")
                                    return False
                    # Booking status: available.
                    book_info.append(i['book_name'])
                    book_info.append(i['author'])
                    return book_info
                check = False
        if not check:
            # The book is not in Books.csv.
            print("Sorry, we don't have a book that you want.")
            print("Please try again")
