#!/usr/bin/env python
import sys
import string

pAvgLength= 0.0
tAvgLength= 0.0
pTotal=0
total= 0
pLength = 0
tLength = 0

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if key == 'pTotal':
		pTotal = int(val)
	elif key == 'total':
		total = int(val)
	elif key == 'pLength':
		pLength = int(val)
	elif key == 'tLength':
		tLength = int(val)

pAvgLength = float(pLength)/float(pTotal)
tAvgLength = float(tLength)/float(total)

print 'Average Tweet Length of President Ono:\t %s' % (pAvgLength)
print 'Average Tweet Length of other users:\t %s' % (tAvgLength)
print 'Total tweets:\t %s' % (total)
print 'Total ptweets:\t %s' % (pTotal)
	
