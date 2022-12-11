import csv
from turtle import Shape, Screen, Turtle
from PIL import Image, ImageTk
from Customer_info import Customer_info
from Rooms import Rooms
from Dessert import Dessert
from Books import Books


room_info = []
choice_room = input("Do you want to book or cancel a room? (Book/Cancel): ")
while choice_room != "Book" and choice_room != "Cancel":
    # If customer do not input Book or Cancel.
    print("please choose again. 🥹")
    choice_room = input("Do you want to book or cancel a room? (Book/Cancel): ")

if choice_room == "Book":
    print("")
    print("1 st Floor: Meeting Zone")
    print("2 nd Floor: Silent Zone")
    print("")
    floor = input("What floor do you want to book? (1/2): ")
    while floor != "1" and floor != "2":
        # If customer choose another choice which not 1 or 2.
        print("Sorry, but we have only 2 floors.")
        floor = input("What floor do you want to book? (1/2): ")

    if floor == "1":
        # Screen → show rooms in floor 1
        screen = Screen()
        screen.setup(width=500, height=650, startx=100, starty=100)
        screen.bgcolor('white')
        img = Image.open("Floor1.png")
        size_w = int(img.width * 0.4)
        size_h = int(img.height * 0.4)
        img = img.resize((size_w, size_h))
        pic = ImageTk.PhotoImage(img)
        screen.addshape('pic', Shape("image", pic))
        tr = Turtle("pic")

        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()
        # Search a room's name inside csv file.
        while not boolean:
            # If it does not find the room's name inside csv file.
            select_room = input("What room do you want?: ")
            customer_select = Rooms(select_room, floor)
            boolean = customer_select.search()
        screen.bye()

    if floor == "2":
        # Screen → show rooms in floor 2
        screen = Screen()
        screen.setup(width=500, height=650, startx=100, starty=100)
        screen.bgcolor('white')
        screen.update()
        img = Image.open("Floor2.png")
        size_w = int(img.width * 0.4)
        size_h = int(img.height * 0.4)
        img = img.resize((size_w, size_h))
        pic = ImageTk.PhotoImage(img)
        screen.addshape('pic', Shape("image", pic))
        tr = Turtle("pic")

        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()
        # Search a room's name inside Rooms.csv and check booking room from json file.
        while not boolean:
            # If it does not find the room's name inside csv file.
            select_room = input("What room do you want?: ")
            customer_select = Rooms(select_room, floor)
            boolean = customer_select.search()
        screen.bye()

    # How long does customer want to book a room?
    hours = int(input("How long do you want to book?(hour(s)): "))
    customer_select = Rooms(select_room, floor)
    price = customer_select.price() * hours
    room_info.append([floor, select_room, hours, price])
    print("")

    # Dessert
    choice_dessert = input("Do you want any dessert?(Yes/No): ")
    dessert_info = []
    while choice_dessert != "Yes" and choice_dessert != "No":
        # If the customer does not choose Yes or No.
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
                # Get desserts information from csv file.
                print(f"{i['list']:^3}|  {i['menu']:<40} {i['price']:>8}.-     ")
            print("----------------------------------------------------------")

        select_dessert = input("Which one do you want to order?(1-10): ")
        dessert = Dessert(select_dessert)
        check = dessert.search()
        # Go to search function in dessert.py, search dessert list in csv file.
        while not check:
            # If customer's order is not 1 to 10.
            select_dessert = input("Which one do you want to order?(1-10): ")
            dessert = Dessert(select_dessert)
            check = dessert.search()

        order = int(input("How many orders do you want?: "))
        print(f"Great choice, You order {order} {check}.")
        price = dessert.price()
        dessert_info.append([check, order, price * order])
        print("")
        choice_dessert = input("Do you want more dessert(Yes/No): ")
        while choice_dessert != "Yes" and choice_dessert != "No":
            # If the customer does not choose Yes or No.
            print("please choose again. 🥹")
            choice_dessert = input("Do you want any dessert?(Yes/No): ")

    if choice_dessert == "No":
        pass
    print("")

    # Book
    choice_book = input("Do you want any interesting books?(Yes/No): ")
    book_info = []
    while choice_book != "Yes" and choice_book != "No":
        # If the customer does not choose Yes or No.
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
                # Get book information from csv file.
                print("")
                print(f"{i['order']:^3}| {i['book_name']:<51}")
                print(f"by {i['author']:<35}")
            print("----------------------------------------------------------")

            select_book = input("Which one do you want to read?(1-20): ")
            book = Books(select_book)
            check_book = book.search()
            # Check information from Books.csv and booking status from json file.
            while not check_book:
                # If customer's order is not 1 to 20.
                select_book = input("Which one do you want to read?(1-20): ")
                book = Books(select_book)
                check_book = book.search()

            if check_book:
                same_book = []
                if len(book_info) != 0:
                    for i in range(len(book_info)):
                        if check_book[0] != book_info[i][0]:
                            same_book.append(False)
                        else:
                            same_book.append(True)
                    if any(same_book):
                        print("You have already chosen this book. 🐨")
                        print("Please try again.")
                    else:
                        print(f"Ok, You want to read '{check_book[0]}' by '{check_book[1]}'.")
                        book_info.append([check_book[0], check_book[1]])

                if len(book_info) == 0:
                    print(f"Ok, You want to read '{check_book[0]}' by '{check_book[1]}'.")
                    book_info.append([check_book[0], check_book[1]])

            print("")
            choice_book = input("Do you want more interesting books?(Yes/No): ")
            while choice_book != "Yes" and choice_book != "No":
                # If the customer does not choose Yes or No.
                print("please choose again. 🥹")
                choice_book = input("Do you want any interesting books?(Yes/No): ")

    if choice_book == "No":
        pass
    print("")

    #  Customer info

    customer_name = input("What is your name-surname?: ")
    customer_nickname = input("What is your nickname?: ")
    customer_phone = input("What is your phone number?: ")
    customer_info = Customer_info(customer_name, customer_nickname, customer_phone, room_info, dessert_info, book_info)
    customer_info.store()
    # Store customer information to json file.
    customer_info.print_bill()
    # Create Bill to print to each customer.

if choice_room == "Cancel":
    # Use customer's name to cancel booking.
    name = input("What is your name-surname? : ")
    database = Customer_info()
    database.cancel(name)
    # Check customer's data from json file.
