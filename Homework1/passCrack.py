import mincemeat
import sys
import md5
import string
import itertools
import hashlib
import string
from string import ascii_lowercase
from string import digits


# Don't forget to start a client!
# ./mincemeat.py -l -p changeme
l=[]
temp=[]
word = sys.argv[1]
for i in range(1,5):
        for combination in itertools.product(ascii_lowercase+digits, repeat=i):
            string=''.join(map(str, combination))
            l.append(string)
finalList = []
chunkSize=len(l)/1000
for i in range(0, len(l),chunkSize) :
    finalList.append(l[i:i+chunkSize])


# The data source can be any dictionary-like object

datasource = dict(enumerate(finalList))

def mapfn(k, v):

  for v1 in v:
    stingcode=hashlib.md5(v1).hexdigest()
    stingcode=stingcode[0:5]
    yield stingcode,v1
    

def reducefn(k, vs):
    #result = sum(vs)
    return list(vs)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

if word in results:
    print "%s is found on %s" % (word, results[word])
else:
    print "%s not found" % word
