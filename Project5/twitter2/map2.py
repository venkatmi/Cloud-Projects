#!/usr/bin/env python

import sys
import string
import json
import operator
total=0
prezono = 'PrezOno'
mon=0
tue=0
wed=0
thu=0
fri=0
sat=0
sun=0
for line in sys.stdin:
	line = line.strip()
	d=json.loads(line)
	try:
		k=d.get(u'user')
		i=k.get(u'screen_name')
		j=d.get(u'created_at')
	except AttributeError:
		continue
	if i == prezono:
		total += 1
		if 'Mon' in j: mon+=1
		elif 'Tue' in j: tue+=1
		elif 'Wed' in j: wed+=1
		elif 'Thu' in j: thu+=1
		elif 'Fri' in j: fri+=1
		elif 'Sat' in j: sat+=1
		elif 'Sun' in j: sun+=1
print 'total\t%s' %(total)
print 'mon\t%s' %(mon)
print 'tue\t%s' %(tue)
print 'wed\t%s' %(wed)
print 'thu\t%s' %(thu)
print 'fri\t%s' %(fri)
print 'sat\t%s' %(sat)
print 'sun\t%s' %(sun)
