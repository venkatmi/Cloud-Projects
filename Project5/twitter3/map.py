#!/usr/bin/env python
import sys
import string
import json
import operator

total=0
pTotal = 0
prezono = 'PrezOno'
tLength = 0
pLength = 0

for line in sys.stdin:
	line = line.strip()
	d=json.loads(line)  
	try:
		
		g=d.get(u'user')
		i=g.get(u'screen_name')
		t=d.get(u'text') 
	except:
                
		continue

	if i == prezono:
		pLength += len(t)
		pTotal += 1
	else:
		tLength += len(t)
		total += 1
		

print 'pTotal\t %s' % (pTotal)
print 'total\t %s' % (total)
print 'tLength\t %s' % (tLength)
print 'pLength\t %s' % (pLength)
