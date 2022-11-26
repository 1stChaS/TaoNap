import csv
from Rooms import Rooms
import Dessert

# better version change to def
# choice_room = input("Do you want to book a room? (Yes/No): ")
# while choice_room != "Yes":
#     if choice_room == "No":
#         # Screen → show a cute turtle swimming for 2 times and ask again
#         pass
#     if choice_room == "Yes":
#         # Screen → show a room number of two floor
#         pass
#     else:
#         print("please choose again. 🥹")
#     choice_room = input("Do you want to book a room? (Yes/No): ")
#
# floor = input("What floor do you want to book? (1/2): ")
# while floor != "1" and floor != "2":
#     print(type(floor))
#     print("Sorry, but we have only 2 floors.")
#     floor = input("What floor do you want to book? (1/2): ")
# if floor == "1":
#     # Screen → show a room of floor 1
#     select_room = input("What room do you want?: ")
#     customer_select = Rooms(select_room, floor)
#     boolean = customer_select.check()
#     while not boolean:
#         select_room = input("What room do you want?: ")
#         customer_select = Rooms(select_room, floor)
#         boolean = customer_select.check()
#
# if floor == "2":
#     # Screen → show a room of floor 2
#     select_room = input("What room do you want?: ")
#     customer_select = Rooms(select_room, floor)
#     boolean = customer_select.check()
#     while not boolean:
#         # check boolean
#         select_room = input("What room do you want?: ")
#         customer_select = Rooms(select_room, floor)
#         boolean = customer_select.check()
#
# hours = int(input("How long do you want to book?(hour(s)): "))
# if isinstance(hours, int):
#     customer_select = Rooms(select_room, floor)
#     price = customer_select.price()*hours
#     print(price)
#
# else:
#     raise ValueError("Hour(s) should be numeric.")

# Dessert

choice_dessert = input("Do you want any dessert?(Yes/No): ")
if choice_dessert == "No":
    pass
if choice_dessert == "Yes":
    with open("Dessert.csv", "r") as file:
        dessert_list = csv.DictReader(file)
        print("-------------------------------------------")
        print(f"{'Dessert':^42}")
        print("-------------------------------------------")
        for i in dessert_list:
            print(f"{i['list']:^3}| {i['menu']:<26} {i['price']:>8}.-")
        print("-------------------------------------------")
    # Screen → The menu of desserts
    select_dessert = input("Which one do you want to order?(1-10): ")
    # go to search function in dessert.py
    order = input("How many orders do you want?: ")
    print(f"Great choice, You order 'two' 'Strawberry shortcakes'.")
    choice_dessert = input("Do you want more dessert(Yes/No): ")

analog_choice_book = input("Do you want any interesting books?(Yes/No): ")
if analog_choice_book == "No":
    pass
if analog_choice_book == "Yes":
    while analog_choice_book == "Yes":
        # Screen → The List of the books
        select_book = input("Which one do you want to read?(1-20): ")
        if select_book:
            print(f"Ok, You want to read 'The Bluest Eye' by 'Toni Morrison'.")
        else:
            print("Oh, sorry for the inconvenience but maybe someone is reading this book now.")
        # Screen → Delete number 4 book. or maybe delete in list is better!
        # Screen → Delete number 4 book.
        analog_choice_book = input("Do you want any interesting books?(Yes/No): ")



# Screen → TAO NAP CARD without name, nickname and phone number
customer_name = input("What is your name - lastname?: ")
customer_nickname = input("What is your nickname?: ")
customer_phone = input("What is your phone number?: ")
# Screen → TAO NAP CARD with name, nickname and phone number
# Screen → The bill of the things that you book.

# Bill


