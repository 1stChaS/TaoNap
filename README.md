# Nap Cafe booking: Tao Nap

![50e1f8624e46cb1a2a14bc89841a0fe0](https://user-images.githubusercontent.com/115055033/205586673-e620c4da-5281-42b9-9e3d-7ac8c3732837.gif)

Hello to anyone and everyone. Welcome to "Tao Nap," my lovely nap cafe. 
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
* Books.csv: the data of books list and author’s name.
* Dessert.csv: the data of desserts menu and desserts’ price.
* Rooms.csv: the data of rooms’ name and rooms’ price.
This project has 6 python files.
* main.py: the main file for asking data from customers.
* Books.py: contains the Books class. This file is used to search what is the book 
            that customers want and check if this book is already booking or not.
