#!/usr/bin/python2.7

import psycopg2
import csv

# Connect to the database.
print "Connecting to the database..."
conn = psycopg2.connect("dbname='mr' user='myrole' host='localhost' password='myrole'")
print "Done!"

# Open a cursor.
cur = conn.cursor()

print ("Check if the table exists...")
try:
	cur.execute("SELECT * FROM classes")
	rows = cur.fetchall()
	print "Done!"
	print "Save the data into csv file..."
	with open('data/result.csv', 'w') as file:
		csv_writer = csv.writer(file, delimiter = ";")
		csv_writer.writerow(["class", "size", "avg_distance"])
		for row in rows:
			csv_writer.writerow([row[0], row[1], row[2]])
	print "Done!"
except:
	print "Error! There is no table called \"classes\""

# Close the connection.
cur.close()
conn.close()
