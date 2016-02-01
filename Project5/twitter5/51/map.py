#!/usr/bin/env python

import sys
import json

d={}

for line in sys.stdin:
    try:
        dic=json.loads(line)
        ids=dic['user']['id_str']
        d[ids]=d.get(ids,0)+1
    except:
        continue

for w in d:
    x=int(w)%10000
    print '%s\t%s\t%s'%(x,w,d[w])




