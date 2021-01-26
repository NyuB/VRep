#!/bin/python

import csv
import sys

file1 = "clean_forum"
file2 = "forum_users"
tab1 = {}
tab2 = {}

for line in sys.stdin:
	params = line.split('\t')
	filename = params[-1]
	
	if file1 in filename:
		key,fields = params[0], params[1:4]
		tab1[key] = fields
	else:
		key,fields = params[0], params[1:4]
		tab2[key]= fields
		
print('-------')

for key1, val1 in tab1.items():
	print(key1,val1)
	if val1[2] in tab2:
		print("{0}\t{1}\t{2}".format(key1, val1, tab2[val1[2]]))