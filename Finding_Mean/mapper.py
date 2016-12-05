#!/usr/bin/python

# Write a mapreduce program that processes the purchases.txt file and outputs mean of sales for each weekday

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want weekday (transformed from element 0 (date)) and element 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)

