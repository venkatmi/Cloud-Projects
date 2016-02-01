#!/usr/bin/env python

import sys
import string
import json
import operator

weekdict=dict()
hourdict=dict()


for line in sys.stdin:
	line = line.strip()
	d=json.loads(line) 
	try:
		c=d.get(u'created_at').split() 
		g=d.get(u'entities') 
		h=g.get(u'hashtags') 
	except:
		continue
	for i in range(len(h)):
		a=h[i] 
		c1=c[3] 
		weekdict.setdefault(c[0],[]).append(a.get(u'text').lower())    
		hourdict.setdefault(c1[:2],[]).append(a.get(u'text').lower()) 
        	

for key,value in weekdict.iteritems(): 
	p=dict()
	q=dict()
	try:
		for v in value:
			p.setdefault(v,[]).append(1)
		for k,v in p.iteritems():
			print '%s\t%s\t%s' % (key,k,sum(v)) 
	except:
		continue

for key,value in hourdict.iteritems(): 
        p=dict()
        q=dict()
	try:
                for v in value:
                        p.setdefault(v,[]).append(1)
                for k,v in p.iteritems():
			print '%s\t%s\t%s' % (key,k,sum(v))
        except:
                continue

	

