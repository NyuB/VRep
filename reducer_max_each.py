import sys
currentKey = None
currentVal = 0
for line in sys.stdin:
	k,v = line.strip().split('\t')
	v=float(v)
	if currentKey is None:
		currentKey = k
		currentVal = v
	elif currentKey == k:
		currentVal=max(currentVal, v)
	else:
		print("{0}\t{1}".format(currentKey,currentVal))
		currentKey = k
		currentVal = v
if currentKey is not None:
	print("{0}\t{1}".format(currentKey,currentVal))