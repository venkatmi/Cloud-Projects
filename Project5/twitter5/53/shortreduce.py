#!/usr/bin/env python

import sys

Short=0
old_hash=None
Short_hash=None
l={}
data={}
avg={}
c={}

def shortd(l):
    Short=1000000
    Short_ids=None
    for w in l:
	if l[w]<Short:
	    Short=l[w]
            Short_ids=w

    return [Short,Short_ids]

def Shortdata(data):
    Short=1000000
    Shortdata=None
    Short_ids=None
    for w in data:
	if data[w][0]<Short:
	    Short=data[w][0]
            Short_ids=data[w][1]
    return [Short,Short_ids]

for line in sys.stdin:
    (hashv,key,val,count)=line.strip().split('\t')
    if old_hash!=hashv:
	data[old_hash]=shortd(avg)
	avg={}
    old_hash=hashv
    try:
	l[key]=l.get(key,0)+int(val)
	c[key]=c.get(key,0)+int(count)
	avg=dict((key,l[key]/c[key]) for key in l)
        
    except:
	continue

data[old_hash]=shortd(avg)
Short=Shortdata(data)

print "Shortest:",Short

