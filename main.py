import csv
import sys
from turtle import Shape, Screen, Turtle
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Taonap_Bill import Customer
from Rooms import Rooms
from Dessert import Dessert
from Books import Books
sys.setrecursionlimit(1500)

# better version change to def
room_info = []
choice_room = input("Do you want to book or cancel a room? (Book/Cancel): ")
while choice_room != "Book" and choice_room != "Cancel":
    print("please choose again. 🥹")
    choice_room = input("Do you want to book a room? (Yes/No): ")
if choice_room == "Cancel":
    img = Image.open('facts-turtles.jpg')
    img.show()
    # looking in csv file


if choice_room == "Book":
    # Screen → show a room number of two floor
    pass

floor = input("What floor do you want to book? (1/2): ")
while floor != "1" and floor != "2":
    print("Sorry, but we have only 2 floors.")
    floor = input("What floor do you want to book? (1/2): ")

if floor == "1":
    # Screen → show a room of floor 1
    wn = Screen()
    wn.setup(width=500, height=650)
    wn.bgcolor('white')

    img = Image.open("Floor1.png")
    # w, h = img.size
    w = int(img.width * 0.4)
    h = int(img.height * 0.4)
    img = img.resize((w, h))
    pic = ImageTk.PhotoImage(img)
    wn.addshape('pic', Shape("image", pic))
    tr = Turtle("pic")
    select_room = input("What room do you want?: ")
    customer_select = Rooms(select_room, floor)
    boolean = customer_select.search()
    while not boolean:
        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()
    wn.bye()

if floor == "2":
    # Screen → show a room of floor 2
    wn = Screen()
    wn.setup(width=500, height=650)
    wn.bgcolor('white')

    img = Image.open("Floor2.png")
    # w, h = img.size
    w = int(img.width * 0.4)
    h = int(img.height * 0.4)
    img = img.resize((w, h))
    pic = ImageTk.PhotoImage(img)
    wn.addshape('pic', Shape("image", pic))
    tr = Turtle("pic")
    select_room = input("What room do you want?: ")
    customer_select = Rooms(select_room, floor)
    boolean = customer_select.search()
    while not boolean:
        # check boolean
        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()
    wn.bye()

hours = int(input("How long do you want to book?(hour(s)): "))
if isinstance(hours, int):
    customer_select = Rooms(select_room, floor)
    # don't show this just check
    price = customer_select.price() * hours

else:
    raise ValueError("Hour(s) should be numeric.")
room_info.append([floor, select_room, hours, price])
print("")

# Dessert

choice_dessert = input("Do you want any dessert?(Yes/No): ")
dessert_info = []
while choice_dessert != "Yes" and choice_dessert != "No":
    print("please choose again. 🥹")
    choice_dessert = input("Do you want any dessert?(Yes/No): ")
while choice_dessert == "Yes":
    # Screen → The menu of desserts
    with open("Dessert.csv", "r") as file:
        dessert_list = csv.DictReader(file)
        print("----------------------------------------------------------")
        print(f"{'ʕ •ᴥ•ʔゝ☆  Dessert  ʕ·ᴥ·　ʔ':^60}")
        print("----------------------------------------------------------")
        for i in dessert_list:
            print(f"{i['list']:^3}|  {i['menu']:<40} {i['price']:>8}.-     ")
        print("----------------------------------------------------------")
    select_dessert = input("Which one do you want to order?(1-10): ")
    dessert = Dessert(select_dessert)
    check = dessert.search()
    # go to search function in dessert.py
    while not check:
        select_dessert = input("Which one do you want to order?(1-10): ")
        dessert = Dessert(select_dessert)
        check = dessert.search()
    order = int(input("How many orders do you want?: "))
    print(f"Great choice, You order {order} {check}.")
    # don't show this just check
    price = dessert.price()
    dessert_info.append([check, order, price * order])
    print("")
    choice_dessert = input("Do you want more dessert(Yes/No): ")
    while choice_dessert != "Yes" and choice_dessert != "No":
        print("please choose again. 🥹")
        choice_dessert = input("Do you want any dessert?(Yes/No): ")
if choice_dessert == "No":
    pass
print("")

# # Book

choice_book = input("Do you want any interesting books?(Yes/No): ")
book_info = []
while choice_book != "Yes" and choice_book != "No":
    print("please choose again. 🥹")
    choice_book = input("Do you want any interesting books?(Yes/No): ")
while choice_book == 'Yes':
    # Screen → The List of the books
    with open("Books.csv", "r") as file:
        data_books = csv.DictReader(file)
        print("----------------------------------------------------------")
        print(f"{'⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ Books ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆':^60}")
        print("----------------------------------------------------------")
        for i in data_books:
            print("")
            print(f"{i['order']:^3}| {i['book_name']:<51}")
            print(f"by {i['author']:<35}")
        print("----------------------------------------------------------")
        select_book = input("Which one do you want to read?(1-20): ")
        book = Books(select_book)
        check_book = book.search()
        while not check_book:
            select_book = input("Which one do you want to read?(1-20): ")
            book = Books(select_book)
            check_book = book.search()
        if check_book:
            print(f"Ok, You want to read '{check_book[0]}' by '{check_book[1]}'.")
            book_info.append([check_book[0], check_book[1]])
            # try to do it again every round should delete book which a customer choose from the menu.
            # Screen → Delete number 4 book. or maybe delete in list is better!
            # Screen → Delete number 4 book.
        print("")
        choice_book = input("Do you want more interesting books?(Yes/No): ")
        while choice_book != "Yes" and choice_book != "No":
            print("please choose again. 🥹")
            choice_book = input("Do you want any interesting books?(Yes/No): ")
if choice_book == "No":
    pass
print("")

#  Customer info

# Screen → TAO NAP CARD without name, nickname and phone number
customer_name = input("What is your name - lastname?: ")  # Chananthida Sopaphol
customer_nickname = input("What is your nickname?: ")  # First
customer_phone = input("What is your phone number?: ")  # 0981027726
customer_info = Customer(customer_name, customer_nickname, customer_phone, room_info, dessert_info, book_info)
bill = customer_info.print_bill()  # Bill
# Screen → TAO NAP CARD with name, nickname and phone number
# Screen → The bill of the things that you book.
