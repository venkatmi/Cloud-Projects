#!/usr/bin/env python
import sys
import string

count = 0
sum1=0
prime=0
old_val = None

for line in sys.stdin:
 (key,val) = line.strip().split('\t',1)
 if old_val != key:
   if old_val:
      print '%s\t%s' % (old_val,count)
   count = 0
 old_val = key
 try:
    count = count + int(val)
 except:
    continue
print '%s\t%s' % (old_val,count)
