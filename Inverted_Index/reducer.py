#!/usr/bin/python

import sys

nodeNum = 0
nodeID = []
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}\t{2}".format(oldKey, nodeNum, nodeID)
        oldKey = thisKey
	nodeNum = 0
        nodeID = []

    oldKey = thisKey
    nodeNum += 1
    nodeID.append(thisVal)

if oldKey != None:
    print "{0}\t{1}\t{2}".format(oldKey, nodeNum, nodeID)

