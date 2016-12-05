#!/usr/bin/python

"""
Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, 
not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.
"""

"""
column names of forum_node.tsv are:
id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, 
last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked

The ones that are the most relevant to the task are:

"id": id of the node
"title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
"tagnames": space separated list of tags
"author_id": id of the author
"body": content of the post
"node_type": type of the node, either "question", "answer" or "comment"
"parent_id": node under which the post is located, will be empty for "questions"
"abs_parent_id": top node where the post is located
"added_at": date added
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
    if len(line) == 19 and line[0] != "id":
	if line[5] == "question":
	    print "{0}\t{1}\t{2}".format(line[0], len(line[4]), 0)
	elif line[5] == "answer":
	    print "{0}\t{1}\t{2}".format(line[6], 0, len(line[4]))

