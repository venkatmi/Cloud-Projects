#!/usr/bin/env python
import sys
import string
import operator
keydict=dict()
for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	v=val.split('\t')
	keydict.setdefault(key,[]).append(v) ##storing all the related key values from map functions
for key,value in keydict.iteritems():
	temp=dict()
	for v in value:
		temp.setdefault(v[0],[]).append(int(v[1])) ##counting the number of hashtags 
	t=max(temp.iteritems(),key=operator.itemgetter(1)) ##printing the most mentioned hashtag in the day or week
	for k,val in temp.iteritems():
		if val==t[1] and k==t[0]:
			print '%s\t%s\t%s' % (key,k,val)
