#!/usr/bin/python

import sys

salesNum = 0
salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the weekday, val is the sale amount
#
# All the sales for a particular weekday will be presented,
# then the key will change and we'll be dealing with the next weekday

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, salesTotal/salesNum)
        oldKey = thisKey
	salesNum = 0
        salesTotal = 0

    oldKey = thisKey
    salesNum += 1
    salesTotal += float(thisVal)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, salesTotal/salesNum)

