#!/usr/bin/python2.7

import sys
import numpy
import json
import pandas
import psycopg2
from sklearn import cluster
import matplotlib.pyplot as plt

# Compute the Euclidean distance from (0, 0).
def distance(i):
	a = x[i]
	b = y[i]
	return numpy.sqrt(a * a + b * b)

# Save new line into the database.
def newLine(i):
	c = 0
	s = 0
	for j in range(len(x)):
		if k_means.labels_[j] == i:
			c = c + 1
			s = s + dist[j]
	sql_command = "INSERT INTO classes VALUES (" + str(i + 1) + ", "
	sql_command = sql_command + str(c) + ", " + str(s/c) + ");"
	cur.execute(sql_command)

# Read the array data.
print "Read the data..."
with open('data/arrays.json', 'r') as file:
	data = json.load(file)
print "Done!"

# Create the arrays x and y.
x = data["x"]
y = data["y"]

# Compute the Euclidean distance from (0, 0) for every (x, y).
dist = []
print "Compute the Euclidean distances..."
for i in range(len(x)):
	dist.append(distance(i))
data = pandas.DataFrame(dist)
print "Done!"

# Use the k means algorithm to divide the data into 5 clusters.
print "Using the k means algorithm..."
k = 0
try:
	k = int(sys.argv[1])
except:
	k = 5
k_means = cluster.KMeans(n_clusters = 5)
k_means.fit(data)
k_means.labels_
print "Done!"

# Connect to the database.
print "Connecting to the database..."
conn = psycopg2.connect("dbname='mr' user='myrole' host='localhost' password='myrole'")
print "Done!"

# Open a cursor.
cur = conn.cursor()

# Drop table classes, if it already exists.
print "Check if it is possible to use that database..."
cur.execute("DROP TABLE IF EXISTS classes;")
print "Done!"

# Create table with SQL.
print "Making the table in the database..."
cur.execute("CREATE TABLE classes (class INT, size INT, avg_distance TEXT);")

# Save the information of classes into PostgreSQL database.
for i in range(5):
	newLine(i)
print "Done!"

# Close the connection.
print "Close the connection..."
conn.commit()
cur.close()
conn.close()
print "Done!"

# Make a color variable for plotting.
colors = []
for i in range(len(x)):
	n = k_means.labels_[i]
	c = 'red'
	if n == 0: c = 'blue'
	elif n == 1: c = 'green'
	elif n == 2: c = 'white'
	elif n == 3: c = 'yellow'
	colors.append(c)

# Make a plot.
print "Make the plot..."
for i in range(len(x)):
	plt.plot(x[i], y[i], 'ro', color = colors[i])
plt.savefig('pic/classes.png')
print "Done!"
