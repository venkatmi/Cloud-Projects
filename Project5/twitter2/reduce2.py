#!/usr/bin/env python

import sys
import string
mon=0
tue=0
wed=0
thu=0
fri=0
sat=0
sun=0
total=0

for line in sys.stdin:
	(key,val) = line.strip().split('\t',1)
	if key == 'mon':
		mon += int(val)
	elif key == 'tue':
		tue += int(val)
	elif key == 'wed':
		wed += int(val)
	elif key == 'thu':
		thu += int(val)
	elif key == 'fri':
		fri += int(val)
	elif key == 'sat':
		sat += int(val)
	elif key == 'sun':
		sun += int(val)
	elif key == 'total':
		total+=int(val)

print 'Total tweets of President Ono:\t %s' % str(total)
print 'Total and Average Tweets for monday:\t %s \t %f' % (str(mon),(float(mon)/float(total)))
print 'Total and Average Tweets for tuesday:\t %s \t %f' % (str(tue),(float(tue)/float(total)))
print 'Total and Average Tweets for wednesday:\t %s \t %f' % (str(wed),(float(wed)/float(total)))
print 'Total and Average Tweets for thursday:\t %s \t %f' % (str(thu),(float(thu)/float(total)))
print 'Total and Average Tweets for friday:\t %s \t %f' % (str(fri),(float(fri)/float(total)))
print 'Total and Average Tweets for saturday:\t %s \t %f' % (str(sat),(float(sat)/float(total)))
print 'Total and Average Tweets for sunday:\t %s \t %f' % (str(sun),(float(sun)/float(total)))
