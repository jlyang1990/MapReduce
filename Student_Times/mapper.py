#!/usr/bin/python

"""
In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:

author_id    hour

For example:

13431511\t13
54525254141\t21

If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. 
The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.
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
	print "{0}\t{1}".format(line[3], line[8][11:13])

