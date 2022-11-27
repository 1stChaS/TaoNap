import csv
from Taonap_Bill import Bill
from Rooms import Rooms
from Dessert import Dessert
from Books import Books

# # better version change to def
room_info = []
choice_room = input("Do you want to book a room? (Yes/No): ")
while choice_room != "Yes":
    if choice_room == "No":
        # Screen → show a cute turtle swimming for 2 times and ask again
        pass
    if choice_room == "Yes":
        # Screen → show a room number of two floor
        pass
    else:
        print("please choose again. 🥹")
    choice_room = input("Do you want to book a room? (Yes/No): ")

floor = input("What floor do you want to book? (1/2): ")
while floor != "1" and floor != "2":
    print(type(floor))
    print("Sorry, but we have only 2 floors.")
    floor = input("What floor do you want to book? (1/2): ")

if floor == "1":
    # Screen → show a room of floor 1
    select_room = input("What room do you want?: ")
    customer_select = Rooms(select_room, floor)
    boolean = customer_select.search()
    while not boolean:
        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()

if floor == "2":
    # Screen → show a room of floor 2
    select_room = input("What room do you want?: ")
    customer_select = Rooms(select_room, floor)
    boolean = customer_select.search()
    while not boolean:
        # check boolean
        select_room = input("What room do you want?: ")
        customer_select = Rooms(select_room, floor)
        boolean = customer_select.search()

hours = int(input("How long do you want to book?(hour(s)): "))
if isinstance(hours, int):
    customer_select = Rooms(select_room, floor)
    # don't show this just check
    price = customer_select.price() * hours
    print(price)

else:
    raise ValueError("Hour(s) should be numeric.")
room_info.append([floor, select_room, hours, price])

# # Dessert

choice_dessert = input("Do you want any dessert?(Yes/No): ")
dessert_info = []
if choice_dessert == "Yes":
    while choice_dessert == "Yes":
        # Screen → The menu of desserts
        with open("Dessert.csv", "r") as file:
            dessert_list = csv.DictReader(file)
            print("-------------------------------------------")
            print(f"{'ʕ •ᴥ•ʔゝ☆ Dessert ʕ·ᴥ·　ʔ':^42}")
            print("-------------------------------------------")
            for i in dessert_list:
                print(f"{i['list']:^3}| {i['menu']:<26} {i['price']:>8}.-")
            print("-------------------------------------------")
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
        print(price)
        print(price * order)
        choice_dessert = input("Do you want more dessert(Yes/No): ")
        dessert_info.append([check, order, price])
if choice_dessert == "No":
    pass

# # Book

choice_book = input("Do you want any interesting books?(Yes/No): ")
book_info = []
while choice_book == 'Yes':
    # Screen → The List of the books
    with open("Books.csv", "r") as file:
        data_books = csv.DictReader(file)
        print("--------------------------------------------------")
        print(f"{'⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ Books ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆':^50}")
        print("--------------------------------------------------")
        for i in data_books:
            print("")
            print(f"{i['order']:^3}| {i['book_name']:<51}")
            print(f"by {i['author']:<35}")
        print("--------------------------------------------------")
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
        choice_book = input("Do you want more interesting books?(Yes/No): ")
if choice_book == "No":
    pass

#  Customer info

# Screen → TAO NAP CARD without name, nickname and phone number
customer_name = input("What is your name - lastname?: ")
customer_nickname = input("What is your nickname?: ")
customer_phone = input("What is your phone number?: ")
customer_info = Bill(customer_name, customer_nickname, customer_phone)
# Screen → TAO NAP CARD with name, nickname and phone number
# Screen → The bill of the things that you book.

# Bill
print("")
print("")
print("")
print("=====================================================================================================")
print("")
print(f"{'TAONAP':^100}")
print(f"{'-- No day is so bad it can’t be fixed with a nap --':^100}")
print("")
print(f"{'  Menu':<60}{'Quantity':^20}{'Price':^20}")
print("-----------------------------------------------------------------------------------------------------")
total_price = []
for i in range(len(room_info)):
    # Floor: 2, Room: P1
    # room_info.append([floor, select_room, hours, price])
    total_price.append(room_info[i][3])
    print(f"  Floor:{room_info[i][0]}, Room:{room_info[i][1]:<40}{room_info[i][2]:^20}{room_info[i][3]:^20}")

for k in range(len(dessert_info)):
    # dessert_info.append([check, order, price])
    total_price.append(dessert_info[k][2])
    print(f"{dessert_info[k][0]:<60}{dessert_info[i][1]:^20}{dessert_info[k][2]:^20}")

for j in range(len(book_info)):
    total_price.append(10)
    print(f"  {book_info[j][0]} - {book_info[j][1]:<40}{'1':^20}{'10':^20}")
print("-----------------------------------------------------------------------------------------------------")
print("")
print(f"Total price: {sum(total_price)} Baht")
print("")
print("")
print(f"Name: {customer_name}")
print(f"Nickname: {customer_nickname}")
print(f"Phone number: {customer_phone}")
print("-----------------------------------------------------------------------------------------------------")
print("")
print(f"{'Thank you! Your booking is confirmed.':^100}")
print(f"{'Have a good day 😊':^100}")
print("")
print("")
print("=====================================================================================================")
