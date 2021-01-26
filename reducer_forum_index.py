#!/usr/bin/python
import sys

currentKey = None
currentList = set()
currentCount = 0

for line in sys.stdin:
	word, nodeId = line.strip().split("\t")
	if currentKey is None:
		currentKey = word
		currentList.add(int(nodeId))
		currentCount+=1
	elif currentKey == word:
		currentList.add(int(nodeId))
		currentCount+=1
	else:
		print("{0}\t{1}\t{2}".format(currentKey,currentCount,currentList))
		currentKey = word
		currentList = set()
		currentList.add(int(nodeId))
		currentCount = 1
if currentKey is not None:
	print("{0}\t{1}\t{2}".format(currentKey,currentCount,currentList))
