#!/usr/bin/python2.7

import sys
import numpy
import json

# Start creating the array data.
print "Create the array data..."

# Create random lists x and y.
x = []
y = []

# Read the length of x and y from command line, if an argument exists.
j = 0
try:
	j = int(sys.argv[1])
except:
	j = 10000 # If there is no argument, let the length be 10.000.

# Fill the lists with random numbers.
for i in range(j):
	x.append(numpy.random.randn())
	y.append(numpy.random.randn())

# Create dictionary of the arrays.
data = {
	'x' : x,
	'y' : y
}
print "Done!"

# Build a json file.
print "Save the array data..."
with open('data/arrays.json', 'w') as file:
	json.dump(data, file, sort_keys = True, indent = 4)
print "Done!"
