#! usr/bin/python
import sys
import csv
post_count = 0
test = 0

a = [line for line in csv.reader(sys.stdin,delimiter='\t')]
a.sort(key=lambda x:len(x[4]), reverse = True)
b = a[:10]
b.sort(key = lambda x : len(x[4]))

print(*b)

