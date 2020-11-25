#!usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer  = csv.writer(sys.stdout, delimiter = '\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	i = line[4]
	pcount = i.count('.') + i.count('!') + i.count('?')
	last = len(i)>0 and i[-1] in ".!?"
	if not(len(i) == 0 or pcount >1 or (pcount == 1 and not(last))):
		writer.writerow(line)

