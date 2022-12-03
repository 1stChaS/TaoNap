import csv
import json


class Books:
    def __init__(self, order):
        self.__order = order

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, new_order):
        if not new_order.isnumeric():
            raise ValueError("Order should be numeric.")
        self.__order = new_order

    def search(self):
        with open("Books.csv", "r") as file:
            data_books = csv.DictReader(file)
            book_info = []
            for i in data_books:
                if self.order == i['order']:
                    try:
                        with open("Customers_info.json", "r") as data_file:
                            data = json.load(data_file)
                    except FileNotFoundError:
                        pass
                    else:
                        for k in data.values():
                            for m in k["Books"]:
                                if m[0] == i['book_name']:
                                    print("Oh, sorry for the inconvenience but someone is reading this book right now.")
                                    return False
                if self.order == i['order']:
                    book_info.append(i['book_name'])
                    book_info.append(i['author'])
                    return book_info
                check = False
        if not check:
            print("Sorry, we don't have a book that you want.")
            print("Please try again")

    # def delete book from file and when the book is return just put it back to csv file and sort it




