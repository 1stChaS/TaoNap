import json


class Customer:
    def __init__(self, customer_name, customer_nickname, customer_phone, book):
        if not customer_name.isalpha():
            raise TypeError("Your name should be string.")
        if not customer_nickname.isalpha():
            raise ValueError("Your nickname should be string.")
        if not customer_phone.isnumeric():
            raise ValueError("Your phone number should be numeric.")
        self.__customer_name = customer_name  # name with surname ex. Chananthida Sopaphol
        self.__customer_nickname = customer_nickname
        self.__customer_phone = customer_phone
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
        elif len(new_phone) != 10:
            raise ValueError("Your phone number should have 10 digits.")
        self.__customer_phone = new_phone

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, new_book):
        self.__book = new_book

    def search(self, Customer_name):
        try:
            with open("Customers_info.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"No data for account number: {Customer_name}")
        else:
            if Customer_name in data:
                print(f"Name={data[Customer_name]['name']},"
                      f" Balance={data[Customer_name]['balance']}")
                # If data exist, it will print out.
            else:
                print(f"No data for account number: {Customer_name}")
                # If data is no longer exist.

    def store(self, Customer_name):
        customer_data = {
            Customer_name.customer_name: {
                "name": Customer_name.customer_name,
                "nickname": Customer_name.customer_nickname,
                "phone number": Customer_name.customer_phone,
                "book": Customer_name.book
            }

        }
        try:
            with open("Customers_info.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("Customers_info.json", "w") as file:
                json.dump(customer_data, file, indent=4)
        else:
            data.update(customer_data)
            with open("Customers_info.json", "w") as file:
                json.dump(data, file, indent=4)

    def cancle(self, Customer_name):
        try:
            with open("Customers_info.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"No data for account number: {Customer_name}")
        else:
            if Customer_name in data:
                for account in list(data):
                    data.pop(account)
                    with open("Customers_info.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                        # Delete Customer's name in json file.
                print(f"DELETE account {Customer_name}")
            else:
                print(f"No data for account number: {Customer_name}")
                # If data is no longer exist.

    def __str__(self):
        return f"name{self.__customer_name}, nickname: {self.__customer_name}, phone number: {self.__customer_name}, " \
               f"book: {self.__customer_name} "
