import json
import Taonap_Bill


class Database:
    def __init__(self, name):
        self.name = name

    def store(self, name):
        customer_data = {
            name.customer_name: {
                "name": name.customer_name,
                "nickname": name.customer_name,
                "phone number": name.customer_phone,
                "book": name.customer_book,
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
            with open()


