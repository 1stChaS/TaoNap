# Nap Cafe booking: Tao Nap

![50e1f8624e46cb1a2a14bc89841a0fe0](https://user-images.githubusercontent.com/115055033/205586673-e620c4da-5281-42b9-9e3d-7ac8c3732837.gif)

> <p>Hello to anyone and everyone. Welcome to "Tao Nap," my lovely nap cafe.</p>
This cafe is a two-floor building. It has two zones.
The first floor is the meeting zone where customers can participate and meet. The first floor is for those who like to read and eat dessert in a cafe atmosphere. 
The second zone is the silent zone. You don't have to speak, talk, or meet anyone; all you have to do is read and sleep peacefully. 
Tao Nap cafe also has a booking books service and also has tasty desserts served for customers.

# Project overview and features
This program is booking the rooms, desserts and books in Tao Nap nap cafe.
The main program: ask for orders from customers and collected in Customers_info.json. 
We have 39 rooms that customers can book. 10 different kinds of tasty dessert and 20 interesting books 
that customers can choose from. Customers can’t choose the same room and books like the others. 
When customers finish ordering. The program will print out the bill. 
Customers can cancel the booking order and it will delete in the json file. 

# Required libraries and tools
I use 4 modules in this project.
* csv, for open and read csv file
* turtle, show the room image.
* PIL, show the room image.
* json, to collect customer data.

# Program design  


# Code structure
This project has 3 csv files.
* [Books.csv](https://github.com/1stChaS/TaoNap/blob/7bc6318714b8598143e0d31af8196ad52741a1da/Books.csv): the data of books list and author’s name.
* [Dessert.csv](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Dessert.csv): the data of desserts menu and desserts’ price.
* [Rooms.csv](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Rooms.csv): the data of rooms’ name and rooms’ price.

<p>This project has 6 python files.</p>

* [main.py](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/main.py): the main file for asking data from customers.
* [Books.py](https://github.com/1stChaS/TaoNap/blob/3e7ff15e8014863ef8edebe011f40506d36b3b2c/Books.py): contains the Books class. This file is used to search what is the book 
            that customers want and check if this book is already booking or not.
* [Dessert.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Dessert.py): contains the Dessert class. This file is used to search what is the dessert 
            that customers want and the dessert's price.
* [Rooms.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Rooms.py): contains the Rooms class. This file is used to search what is the room 
            that customers want, check if this room is already booking or not and the room's price.
* [Taonap_Bill.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Taonap_Bill.py): contains Bill class. This file used to store customers' data to json file and print out text bills.
* [Cancel.py](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Cancel.py): contains the Cancel class. This file used to cancel the customer data from [Customers_info.json](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Customers_info.json) file.

<p>This project has 1 JSON file.</p>

* [Customers_info.json](https://github.com/1stChaS/TaoNap/blob/9283f69a88d5c3eebffe449eb5e96d10ac8dfa31/Customers_info.json)

Example bill: 
[Text file](https://github.com/1stChaS/TaoNap/blob/1553ee82b97bd139eb010e8b9af17ce9836a7fd2/lady04-Dec-2022_00:08:28.txt)     
