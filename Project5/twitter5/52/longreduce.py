#!/usr/bin/env python

import sys

Long=0
old_hash=None
Long_hash=None
l={}
data={}
avg={}
c={}

def longd(avg):
    Long=0
    Long_ids=None
    for w in avg:
	if avg[w]>Long:
	    Long=avg[w]
            Long_ids=w

    return [Long,Long_ids]

def longdata(data):
    Long=0
    longdata=None
    Long_ids=None
    for w in data:
	if data[w][0]>Long:
	    Long=data[w][0]
            Long_ids=data[w][1]
    return [Long,Long_ids]

for line in sys.stdin:
    (hashv,key,val,count)=line.strip().split('\t')
    if old_hash!=hashv:
	data[old_hash]=longd(avg)
	avg={}
    old_hash=hashv
    try:
	l[key]=l.get(key,0)+int(val)
	c[key]=c.get(key,0)+int(count)
	avg=dict((key,l[key]/c[key]) for key in l)
	
    except:
	continue
   
data[old_hash]=longd(avg)

Long=longdata(data)

print "Longest:",Long

