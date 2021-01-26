#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
res=0
for line in reader:
	if len(line) > 0:
		res+=1
	print(res)
print(res)
