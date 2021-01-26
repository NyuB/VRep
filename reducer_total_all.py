import sys
currentVal = 0
for line in sys.stdin:
	k,v = line.strip().split('\t')
	v=float(v)
	currentVal+=v
print(currentVal)