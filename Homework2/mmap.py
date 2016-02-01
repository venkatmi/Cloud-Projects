#!/usr/bin/env python
import sys
import math
import os

count = 0
prime=0
sum1=0

for line in sys.stdin:
  nos = int(line.strip())
  sq=int(math.sqrt(nos))
  count += 1
  sum1+=nos
  
  flag=0

  if nos==0 or nos==1:
       flag=1
  elif nos!=2 and nos%2==0:
      flag=1
  elif nos==2:
      flag=0
  else:
   for i in xrange(3,sq+1,2):
    if nos%i==0:
         flag=1
         break
  if flag==0: 
    prime+=1
   

print 'Count\t%s' % str(count)
print 'Sum\t%s' % str(sum1)
print 'Prime\t%s' %str(prime)
