import sys
currentKey = None
currentVal = 0
currentCount = 0
for line in sys.stdin:
	k,v = line.strip().split('\t')
	v=float(v)
	if currentKey is None:
		currentKey = k
		currentVal = v
		currentCount = 1
	elif currentKey == k:
		currentVal += float(v)
		currentCount += 1
	else:
		print("{0}\t{1}".format(currentKey,currentVal/currentCount))
		currentKey = k
		currentVal = v
		currentCount = 1
if currentKey is not None:
	print("{0}\t{1}".format(currentKey,currentVal/currentCount))