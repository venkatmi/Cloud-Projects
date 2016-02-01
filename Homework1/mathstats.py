import mincemeat
import sys
import math as ma 
import os

arg1 = sys.argv[1]
file = open(arg1,'r')
data = list(file)
file.close()
finalList=[]
chunkSize=len(data)/3
for i in range(0, len(data),chunkSize) :
    finalList.append(data[i:i+chunkSize])

# The data source can be any dictionary-like object
datasource = dict(enumerate(finalList))

def mapfn(k, v):
    for vi in v:
    #v=int(v.rstrip(os.linesep))
      vi=int(vi.strip())
      yield 1,vi
    

def reducefn(k, vs):
    std=0
    result=0
    count=len(vs)
    result = sum(vs)
    mean=result/count
    #sd=sum((vs-mean)*(vs-mean))
    for v in vs:
        std=std+((v-mean)**2)
    sdev=(std/count-1)**(0.5)
    return count,result,sdev

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn


results = s.run_server(password="changeme")

print 'count :'+ str(results[1][0])
print 'sum :'+str(results[1][1])
print 'standard deviation :'+str(results[1][2])
