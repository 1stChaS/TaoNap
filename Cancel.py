import json


class Customer:
    def __init__(self, name):
        self.__name = name

    @property
    def customer_name(self):
        return self.__name

    @customer_name.setter
    def customer_name(self, new_name):
        self.__name = new_name

    def cancle(self, Customer_name):
        try:
            with open("Customers_info.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print(f"Don't have the data")
        else:
            if Customer_name in data:

                for name in list(data):
                    print(f"Hello! {Customer_name}")
                    print(f"You book room: {data[Customer_name]['Room']}")

                    if len(data[Customer_name]['Books']) != 0:
                        print("You also read ")
                        book_info = [i for i in data[Customer_name]['Books']]
                        for i in range(len(book_info)):
                            print(f"{i+1}. {book_info[i][0]} "
                                  f"by {book_info[i][1]}")
                        choose = input("Are you really want to cancel this room?(Yes/No): ")
                        while choose != "Yes" and choose != "No":
                            print("please choose again. 🥹")
                            choose = input("Are you really want to cancel this room?(Yes/No): ")
                        if choose == "Yes":
                            print(f"Cancel room: {data[Customer_name]['Room']}")
                            data.pop(name)
                            with open("Customers_info.json", "w") as data_file:
                                json.dump(data, data_file, indent=4)
                                # Delete Customer's name in json file.
                        if choose == "No":
                            print("Thank you for not cancel 🙏🏼")
                    print("THANKYOU FOR YOU SUPPORT 🫀")
            else:
                print(f"No data for account number: {Customer_name}")


