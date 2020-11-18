#!/usr/bin/python
import sys
salesTotal = 0
oldKey = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey is not None and oldKey !=thisKey: #On considere les inputs deja triees par clef(role du sorter/shuffler)
		print "{0}\t{1}".format(oldKey,salesTotal)
		salesTotal = 0
	oldKey = thisKey
	salesTotal += float(thisSale)
	if oldKey is not None:
		print oldKey, '\t', salesTotal
