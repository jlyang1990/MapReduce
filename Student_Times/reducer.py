#!/usr/bin/python

import sys

def findHourList(hourDic):
    hourNum = 0
    hourList = []
    for h in hourDic:
	if hourDic[h] > hourNum:
	    hourNum = hourDic[h]
	    hourList = [h]
	elif hourDic[h] == hourNum:
	    hourList.append(h)
    return hourList

hourDic = {}
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
	hourList = findHourList(hourDic)
	for h in hourList:
            print "{0}\t{1}".format(oldKey, int(h))
        hourDic = {}

    oldKey = thisKey
    if thisVal not in hourDic:
	hourDic[thisVal] = 1
    else:
	hourDic[thisVal] += 1

if oldKey != None:
    hourList = findHourList(hourDic)
    for h in hourList:
        print "{0}\t{1}".format(oldKey, int(h))

