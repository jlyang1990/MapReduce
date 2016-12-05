#!/usr/bin/python

import sys

queLen = 0
ansLen = 0
lenNum = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal1, thisVal2 = data_mapped

    if oldKey and oldKey != thisKey:
	if lenNum == 1:
	    print "{0}\t{1}\t{2}".format(oldKey, queLen, 0)
	else:
	    print "{0}\t{1}\t{2}".format(oldKey, queLen, float(ansLen)/(lenNum-1))
	queLen = 0
	ansLen = 0
	lenNum = 0

    oldKey = thisKey
    queLen += int(thisVal1)
    ansLen += int(thisVal2)
    lenNum += 1

if oldKey != None:
    if lenNum == 1:
	print "{0}\t{1}\t{2}".format(oldKey, queLen, 0)
    else:
	print "{0}\t{1}\t{2}".format(oldKey, queLen, float(ansLen)/(lenNum-1))

