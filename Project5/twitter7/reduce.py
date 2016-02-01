#!/usr/bin/env python
import sys
import string

count = 0.0
sum1=0
prime=0
old_val = None
old=dict()

for line in sys.stdin:
 (key,val) = line.strip().split('\t',1)
 if old_val != key:
   if old_val:
      #print '%s\t%s' % (old_val,count)
      old[old_val]=float(count)
   count = 0
 old_val = key
 try:
    count = count + float(val)
 except:
    continue


#print '%s\t%s' % (old_val,count)
old[old_val]=count

lat=float(old['latt'])/float(old['points'])
lon=float(old['long'])/float(old['points'])
print 'lattitude\t%s' % (lat)
print 'longitude\t%s' % (lon)
print 'points\t%s' %str(old['points'])
print 'rest\t%s' %str(old['rest'])
print 'total\t%s' %str(old['total'])






