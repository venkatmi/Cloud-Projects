#!/usr/bin/env python
import sys

Max=0
Max_hash=None
old_hash=None
d={}
dic={}
def maxd(d):
    Max =0
    Max_ids=None
    for w in d:
        if d[w]>Max:
            Max=d[w]
            Max_ids=w
 
    return [Max,Max_ids]

def maxdic(dic):
    Max=0
    Maxdic=None
    for w in dic:
        if dic[w][0]>Max:
            Max=dic[w][0]
            Max_ids=dic[w][1]
    return [Max,Max_ids]
        

for line in sys.stdin:
    (hashv,key,val)=line.strip().split("\t")
    if old_hash !=hashv:
        dic[old_hash]=maxd(d)
        d={}
    old_hash=hashv
    try:
        d[key]=d.get(key,0)+int(val)
    except:
        continue

dic[old_hash]=maxd(d)
 
Max= maxdic(dic)
    

print "Max:",Max

