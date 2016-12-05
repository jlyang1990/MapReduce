#!/usr/bin/python

"""
In this exercise your task is to write a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) 
would give us a list of students that have posted there - either asked the question, answered a question or added a comment. 
If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
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
	    print "{0}\t{1}".format(line[0], line[3])
	else:
	    print "{0}\t{1}".format(line[6], line[3])

