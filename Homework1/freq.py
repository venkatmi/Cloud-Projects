import mincemeat
import os
import sys
# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

arg1 = sys.argv[1]
file = open(arg1,'r')
data = list(file)
file.close()


# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    v=v.rstrip(os.linesep)
    for word in v:
      #word = word.strip()
      yield word.lower(), 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []
total=0
for k in results.keys():
  resultlist.append((k,results[k]))
  total=total+results[k]
resultlist = sorted(resultlist, key=lambda a: a[1])

for a,a1 in resultlist:
    print '%s'%str(a),'%s'%str(a1),'%.2f'%((float(a1)/float(total))*100),'%'
 
