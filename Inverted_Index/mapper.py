#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
    if len(line) == 19 and line[0] != "id":
        words = re.compile('[a-zA-Z]+').findall(re.sub('<[^>]*>', '', line[4].lower()))
        for word in words:
	    print "{0}\t{1}".format(word, line[0])

