from csv import reader
with open('csvfile.csv') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
