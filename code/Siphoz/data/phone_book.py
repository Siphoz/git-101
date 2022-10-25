import csv

with open('phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    for row in csv_reader:
        print (row['first_name'],":", int(row['phone_number']))
