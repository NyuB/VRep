#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QHOTE_ALL)

a = []

for line in reader:
	a.append(line[4])
a.sort(key = lambda x : len(x), reverse=True)
a = a[0:10]

for ai in a:
	print(ai)
