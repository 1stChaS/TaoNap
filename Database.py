# import json
#
#
# class Database:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     def search(self, Customer_name):
#         try:
#             with open("accounts.json", "r") as data_file:
#                 data = json.load(data_file)
#         except FileNotFoundError:
#             print(f"No data for account number: {Customer_name}")
#         else:
#             if Customer_name in data:
#                 print(f"Name={data[Customer_name]['name']},"
#                       f" Balance={data[Customer_name]['balance']}")
#                 # If data exist, it will print out.
#             else:
#                 print(f"No data for account number: {Customer_name}")
#                 # If data is no longer exist.
#
#     def store(self, Customer_name):
#         customer_data = {
#             Customer_name.customer_name: {
#                 "name": Customer_name.customer_name,
#                 "nickname": Customer_name.customer_name,
#                 "phone number": Customer_name.customer_phone,
#                 "book": Customer_name.customer_book,
#             }
#
#         }
#         try:
#             with open("Customers_info.json", "r") as file:
#                 data = json.load(file)
#         except FileNotFoundError:
#             with open("Customers_info.json", "w") as file:
#                 json.dump(customer_data, file, indent=4)
#         else:
#             data.update(customer_data)
#             with open("Customers_info.json", "w") as file:
#                 json.dump(data, file, indent=4)
#
#     def cancle(self, Customer_name):
#         try:
#             with open("accounts.json", "r") as data_file:
#                 data = json.load(data_file)
#         except FileNotFoundError:
#             print(f"No data for account number: {Customer_name}")
#         else:
#             if Customer_name in data:
#                 for account in list(data):
#                     data.pop(account)
#                     with open("accounts.json", "w") as data_file:
#                         json.dump(data, data_file, indent=4)
#                         # Delete Customer's name in json file.
#                 print(f"DELETE account {Customer_name}")
#             else:
#                 print(f"No data for account number: {Customer_name}")
#                 # If data is no longer exist.
#
#
#
