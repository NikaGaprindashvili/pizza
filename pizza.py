import sys
import os
import csv
from tabulate import tabulate

# check for command-line argument
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) != 2:
    sys.exit("Too many command-line arguments")

# check that the argument is a CSV file
filename = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

# check that the file exists
if not os.path.isfile(filename):
    sys.exit("File does not exist")

# read the CSV file into a list of dictionaries
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# format the data as an ASCII art table
table = tabulate(data, headers="keys", tablefmt="grid")

# print the table
print(table)
