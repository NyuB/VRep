#!/bin/python

import csv
import sys
import os
reader = csv.reader(sys.stdin, delimiter='\t')
file1 = "clean_forum"
first_line_file1 = True
file2 = "forum_users"
first_line_file2 = True
file_name = file1
for data in reader:
	if(len(data)==0):
		continue
	if len(data) >= 10:
		file_name = file1
	else:
		file_name = file2
	if file1 in file_name:
		if first_line_file1 or len(data) <= 9:
			first_line_file1 = False
			continue
		fields = data[1:4]
		print("{0}\t{1}\t{2}\t{3}\t{4}".format(data[0], fields[0], fields[1], fields[2], file1))	
	elif file2 in file_name:
		if first_line_file2 or len(data) <= 4:
			first_line_file2 = False
			continue
		print("{0}\t{1}\t{2}\t{3}\t{4}".format(data[0], data[1],data[2],data[3], file2))