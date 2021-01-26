#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
a = []
for line in reader:
	if len(line) > 0:
		a.append(line[4])
a.sort(key = lambda x : len(x), reverse=True)
a = a[0:10]

print('')
for ai in a:
	print("\n===========================================\n")
	print(ai)
