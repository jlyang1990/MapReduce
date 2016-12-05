#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        
    user_ptr_id = ""
    author_id = ""

    for line in reader:
        
        if line[1] == "A":
            try:
                user_ptr_id,marker,reputation,gold,silver,bronze = line
            except:
                print "ERROR in forum users"
                pass
        if line[1] == "B":
            try:
                author_id,marker,id,title,author_id,tagnames,node_type,parent_id,abs_parent_id,added_at,score = line
            except:
                print "ERROR in forum nodes"
                pass

        try:
            if user_ptr_id == author_id:
                temp = [id,title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,silver,bronze]
                writer.writerow(temp)
        except:
            print "ERROR in matching users and nodes"
            pass