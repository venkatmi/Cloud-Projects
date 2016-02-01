#!/usr/bin/env python
import sys
import string
import json
import operator
userdict=dict()
countdict=dict()
for line in sys.stdin:
    line = line.strip()
    d=json.loads(line)  ## main dictionary which contains the entire tweet data
    try:
    	d1=d.get(u'retweeted_status')
    	f=d1.get(u'created_at').split()
    	c=d1.get(u'text')
	c=c.replace('\n','')
	g=d1.get(u'retweet_count') ## loading the entities information into another dictionary
	h=d1.get(u'favorite_count')
    except:
        continue
    c1=f[1]+str(f[2])
    if g>h:
        h=g
    if c1 in userdict.keys():
            t=userdict[c1].split('\t')
            if int(t[1])<h:
                c2=c+'\t'+str(h)
                userdict[c1]=c2
    else:
             c2=c+'\t'+str(h)
             userdict[c1]=c2
	# adding for the corresponding hour
for k,v in userdict.iteritems():
	print '%s\t%s' % (k,v)
