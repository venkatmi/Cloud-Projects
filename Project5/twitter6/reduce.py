#!/usr/bin/env python

import sys
import string
import operator

keydict=dict()


for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	v=val.split('\t')
	keydict.setdefault(key,[]).append(v)


for key,value in keydict.iteritems():
	temp=dict()
	temp2=dict()
	for v in value:
		temp.setdefault(v[0],[]).append(int(v[1])) 
		for p,q in temp.iteritems():
			temp2.update({p:sum(q)})
	t=max(temp2.iteritems(),key=operator.itemgetter(1)) 
        
	for k,val in temp2.iteritems():
		if val==t[1] and k==t[0]:
			print '%s\t%s\t%s' % (key,k,val)


	
			
	

