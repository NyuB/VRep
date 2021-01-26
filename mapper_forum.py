#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

P = ".!?"

def countAll(msg,l):
	res = 0
	for c in l:
		res+=msg.count(c)
	return res

def isPhrase(msg):
	if len(msg) == 0:
		return False
	c = countAll(msg,P)
	if c>1:
		return False
	elif c==0:
		return True
	elif not(msg[-1] in P):
		return False
lines = []
for line in reader:
	msg = line[4]
	if isPhrase(msg):
		writer.writerow(line)
