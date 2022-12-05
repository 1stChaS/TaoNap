# Nap Cafe booking: Tao Nap

![50e1f8624e46cb1a2a14bc89841a0fe0](https://user-images.githubusercontent.com/115055033/205586673-e620c4da-5281-42b9-9e3d-7ac8c3732837.gif)

> <p>Hello everyone! Welcome to "Tao Nap," my lovely nap cafe.</p>
This cafe is a two-floor building. It has two zones.</br>
*The first floor* is the meeting zone where customers can participate and chat. The first floor is for those who like to read and eat dessert in a cafe atmosphere.</br> 
*The second zone* is the silent zone. You don't have to speak, talk, or meet anyone; all you have to do is read and sleep peacefully.</br>
Tao Nap cafe also has a booking books service and also has tasty desserts served for customers.</br>

# Project overview and features
This program is booking the rooms, desserts and books in Tao Nap nap cafe.</br>
The main program: ask for orders from customers and collected in Customers_info.json.</br> 
We have 39 rooms that customers can book. 10 different kinds of tasty dessert and 20 interesting books 
that customers can choose from. Customers can’t choose the same room and books like the others.</br>
When customers finish ordering. The program will print out the bill.</br>
Customers can cancel the booking order.</br> 

# Required libraries and tools
I use 4 modules in this project.
* `csv` : for open and read csv file
* `turtle` : show the room image.
* `PIL` : show the room image.
* `json` : to collect customer data.

# Program design  
<p>This project has 4 classes.</p>

![Blank diagram-2](https://user-images.githubusercontent.com/115055033/205624214-ef7223db-7ea3-4bbe-b843-9d9c6006133d.png)

+ `Books` : The search method will check order(string) attribute from csv file which this order is in csv file or not. If True it will check in the json file, if this book is already booked, It will return False. If it available, it will return list.
+ `Dessert` : The search method will check menu(string) attribute from the csv file. If this dessert is in csv file, It will return True with the dessert's name. The price method will check the price of the dessert.
+ `Rooms` : The search method will check room_name(string) attribute from csv file which this room_name is in csv file or not. If True it will check in the json file, if this room is already booked, It will return False. If it available, it will return True. The price method will check the price of the room.
+ `Customer_info` : The store method store customer's booking data. The print_bill method will print out each customer bill. The cancel method will delete data of customer who is name(string) attribute.

# Code structure
This project has 3 csv files.
* [Books.csv](https://github.com/1stChaS/TaoNap/blob/7bc6318714b8598143e0d31af8196ad52741a1da/Books.csv): the data of books list and author’s name.
* [Dessert.csv](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Dessert.csv): the data of desserts menu and desserts’ price.
* [Rooms.csv](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Rooms.csv): the data of rooms’ name and rooms’ price.

<p>This project has 5 python files.</p>

* [main.py](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/main.py): the main file for asking data from customers.
* [Books.py](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Books.py): contains the **Books class**. This file is used to search what is the book 
            that customers want and check if this book is already booking or not.
* [Dessert.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Dessert.py): contains the **Dessert class**. This file is used to search what is the dessert 
            that customers want and the dessert's price.
* [Rooms.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Rooms.py): contains the **Rooms class**. This file is used to search what is the room 
            that customers want, check if this room is already booking or not and the room's price.
* [Customer_info.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Taonap_Bill.py): contains **Bill class**. This file used to store customers' data to json file, cancel and print out text bills.

<p>This project has 1 JSON file.</p>

* [Customers_info.json](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Customers_info.json)

Example bill: 
[Text file](https://github.com/1stChaS/TaoNap/blob/13429c51a8ddde19a08c9d3adb4af589149172a3/lady05-Dec-2022_17:53:29.txt)     
