#!/usr/bin/python

import sys

stuList = []
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
	print "{0}\t{1}".format(oldKey, stuList)
        stuList = []

    oldKey = thisKey
    stuList.append(thisVal)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, stuList)
