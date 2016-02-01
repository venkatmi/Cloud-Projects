#!/usr/bin/env python
import sys
import string

sent_count = 0
sum1=0
#avg=0.0


for line in sys.stdin:
 (key,val) = line.strip().split('\t',1)
 if key=='sentence':
   sent_count=sent_count+int(val)
 else:
   sum1=sum1+int(val)

#avg=float(sent_count/sum1)
print '%s\t%s' % ('count',sum1)
print '%s\t%s' % ('avg',float(sent_count)/float(sum1))
