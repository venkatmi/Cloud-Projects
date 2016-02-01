#!/usr/bin/env python

import sys
import json
import string

d={}
l={}


for line in sys.stdin:
    line=line.strip()
    try:
        data=json.loads(line)
	
	ids=data['user']['id_str']
	
	text=data['text']
	
	d[ids]=d.get(ids,0)+1
	
	l[ids]=l.get(ids,0)+len(text)
	
	
	
		
    except:
	continue

for w in d:
    x=int(w)%10000
    print '%s\t%s\t%s\t%s'%(x,w,l[w],d[w])
    
    
