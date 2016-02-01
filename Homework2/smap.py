#!/usr/bin/env python
import sys
import string
import os

sent = 0
flag=0
count=0
for line in sys.stdin:
  import re
  line = (line.strip())
  for word in line:
   ch=str(word[0])
   if count>=1 and flag==1:
     #count+=len(str(word))
     if (word[0].isupper()):
       count=1
     else:
       count+=1
       if re.match('[\.\!?]',ch):
         print 'sentence\t%s'%str(count)
         print 'count\t%s'%str(1)
         count=0
         flag=0
   
       
   else:   
      if (word[0].isupper()):
           #count=len(str(word))
           count+=1
           flag=1
if count>=1:
 print 'sentence\t%s'%str(count)
 print 'count\t%s'%str(1)
