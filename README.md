# Data-analysis-with-Python

This is a little data analysis project with Python and PostgreSQL. If you want to test the codes, please make a new database in PostegreSQL with the following instructions:
- Username: myrole
- Password: myrole
- Host: localhost
- Port: 5432
- Database: mr

The very first file is data_generator.py. It includes a code that creates two arrays, x and y, and fills them with random numbers. You can give the length of x and y as a command line parameter, but if that parameter is missing, then the length will be 10.000. When the arrays have been created, they will be saved into data folder in a file named arrays.json.

When the arrays.json file is created and the database settings are okay, then you can run the code in data_analysis.py. This code reads the file arrays.json, computes the Euclidean distance from (0, 0) for every (x, y) in arrays.json file and completes k means algorithm with default k = 5 (you can change the value of k by giving the new value as a command line argument). After that, the code takes a connection to PostgreSQL, computes the sizes and average distances of every class and saves these infos into database. Finally it makes a plot of the distances and uses different colors by the classes.

The last file, data_save.py, reads the data from database (if it exists there) and makes a csv file of it. This file goes also into the data folder with name result.csv.

There are the example files in the data and pic folders. They are results of the analysis in which the length of x and y is 10.000 and k = 5. That kind of analysis can be done with the following command:

$ python data_generator.py 10000; python data_analysis.py 5; python data_save.py

Because 10.000 and 5 are the defaults, this command does also the same kind of analysis:

$ python data_generator.py; python data_analysis.py; python data_save.py
