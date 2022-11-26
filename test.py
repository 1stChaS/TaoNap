import csv
with open('Rooms.csv', "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for i in csv_reader:
        print(i['floor'])