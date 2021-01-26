#!/usr/bin/python
import csv
import sys
import re

reader = csv.reader(sys.stdin, delimiter='\t')

lines = []
first = True
wreg = r"[\w']+|[.,!?;]"
exclude = ['.','!','?','-','#',"$","{",'}','(',')','=','<','>',':',';','/']

limit = 10000
cur = 1
for line in reader:
	if(first):
		first = False
		continue
	if cur>limit:
		break
	cur+=1
	msg = line[4]
	nodeId = line[0]
	words = re.findall(wreg,msg)
	for w in words:
		if not(w in exclude):
			print("{0}\t{1}".format(w.lower(), nodeId))
