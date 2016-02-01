#!/usr/bin/env python
import sys
import string
import json
import operator

latt=0
longt=0
points=0
others=0
total=0

for line in sys.stdin:
	line = line.strip()
       
        
        total+=1
	d=json.loads(line)  
	try:
		
		g=d.get(u'geo')
		h=g.get(u'coordinates') 
	except:
                others+=1
		continue
        
        if len(h)>0 and len(h)==2:
            lat=h[0]
            longi=h[1]
	    latt+=lat 
	    longt+=longi
            points+=1
        else:
            others+=1
       
print 'latt\t %s' % str(latt)
print 'long\t %s' % str(longt)
print 'total\t %s' %str(total)
print 'points\t %s' %str(points)
print 'rest\t %s' %str(others)



 
