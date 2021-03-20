import csv

with open('ClassStats.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        print(row)