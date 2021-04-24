import csv
with open('CSV files/My_File.csv', 'rt') as file:
    csv_rows = csv.reader(file)
    for row in csv_rows:
        print(row)
