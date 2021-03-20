import csv
import db_api

with open('ClassStats.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        #print()
        x = 1

db = db_api.Database(host='localhost', user='root', password='aCorn9811!', database='testing')

db.close_connection()