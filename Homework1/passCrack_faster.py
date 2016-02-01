import mincemeat
import sys
import md5
import string
import itertools
import hashlib
import string
from string import ascii_lowercase
from string import digits

data=[]
word = sys.argv[1]
data.append(word)

# The data source can be any dictionary-like object

datasource = dict(enumerate(data))

def mapfn(k, v):
  import itertools
  import hashlib
  import string
  from string import ascii_lowercase
  from string import digits

  for i in range(1,5):
        for combination in itertools.product(ascii_lowercase+digits, repeat=i):
            string=''.join(map(str, combination))
            stingcode=hashlib.md5(string).hexdigest()
            stingcode=stingcode[0:5]
            
            if stingcode==v:
                yield stingcode,string
    

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
