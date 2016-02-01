#!/usr/bin/env python
import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import urlparse
import sys
import urllib
import string
import math

PORT_NUMBER=80
def distance_on_unit_sphere(lat1, long1, lat2, long2):
    
    degrees_to_radians = math.pi/180.0
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    arc=arc*3690

    return arc

def fetchdetails(self,nam,zipcode):
    #self.wfile.write('hi')
    count=1
    songlst=[]
    r=urllib.urlopen('http://developer.echonest.com/api/v4/artist/profile?api_key=OQWYYBIAMT08XEK1J&name='+nam+'&bucket=genre&bucket=songs&bucket=hotttnesss&bucket=id:songkick&format=json').read()
    r=json.loads(r)
    #self.wfile.write(r)
    for j in r['response']['artist']['foreign_ids']:
        artistid=j['foreign_id']
    
    artistid=string.split(artistid,":")
    artist=artistid[2]
    self.wfile.write("Artist :"+r["response"]['artist']["name"]+'\n')
    self.wfile.write("Popularity :"+str(r["response"]['artist']["hotttnesss"])+'\n')
    #self.wfile.write(artist)
    self.wfile.write('Top Songs of the artist: \n')
    for i in r["response"]['artist']["songs"]:
        if i["title"].lower() not in songlst:
            self.wfile.write(str(count)+' : '+i["title"]+'\n')
            songlst.append(i["title"].lower())
            count =count+1
    self.wfile.write('\n\n')
    if artist is None:
        self.wfile.write('Error...artist name missing')
    return artist

def fetchevent(self,nam,zipcode,arid):
    eventname=[]
    eventloc=[]
    eventdis=[]
    eventtime=[]
    r1=urllib.urlopen('http://api.songkick.com/api/3.0/artists/'+str(arid)+'/calendar.json?apikey=X16HfvTA28vSWIex')
    r2=r1.read()
    r2=json.loads(r2)
    #json_string = json.dumps(r2,sort_keys=True,indent=2)
    #events=r2["event"]
    zi=urllib.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+str(zipcode)+'&sensor=false').read()
    zi=json.loads(zi)
    #self.wfile.write(zi["results"])
    for i in zi["results"]:
        #self.wfile.write(i['geometry'])
        lat1=i['geometry']["location"]["lat"]
        long1=i['geometry']["location"]["lng"]
    try:
     for item in r2["resultsPage"]["results"]["event"]:
      try:
        
        #self.wfile.write(item['location']['city']+'\n')
        lat2=item['location']["lat"]
        long2=item['location']["lng"]
       # self.wfile.write(str(lat2)+'\n')
        #self.wfile.write(str(long2)+'\n')
        dist=distance_on_unit_sphere(lat1, long1, lat2, long2)
        #self.wfile.write(str(dist)+'\n')
        eventdis.append(dist)
        eventname.append(item['displayName'])
        eventloc.append(item['location']['city'])
        eventtime.append(item['start']['datetime'])
      except:
        continue
    except:
     self.wfile.write('This artist has no future events !!')
     sys.exit()
    op=min(eventdis,key=float)
    index1=eventdis.index(op)
    evname=eventname[index1]
    evloc=eventloc[index1]
    evtime=string.split(eventtime[index1],'T')
    self.wfile.write('Nearest Event to the given zipcode Name :'+evname+'\n')
    self.wfile.write('Date : '+str(evtime[0])+'\n')
    self.wfile.write('time '+str(evtime[1])+'\n')
    self.wfile.write(evloc+'\n')
    self.wfile.write(str(op)+' miles'+'\n')
    if eventname is []:
        return 0
        
    else :return 1
    

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      try:
        if self.path.startswith("/favartist"):
            o=urlparse.urlparse(self.path)
            getvars=urlparse.parse_qs(o.query)
            name=str(getvars['name'][0])
            zipcode=int(getvars['zipcode'][0])
        
            try:
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                #name=str(getvars['name'][0])
                #zipcode=int(getvars['zipcode'][0])
                #self.wfile.write('hi',name,zipcode)
                arid=fetchdetails(self,name,zipcode)
                #self.wfile.write(r)
                r1=fetchevent(self,name,zipcode,arid)
                if r1 is 0:
                    self.wfile.write('No events found !!!')
                    #sys.exit()
            except ArithmeticError:
                e=sys.exc_type()
                self.send_error(404,'Error')
                sys.exit()
      except:
        self.wfile.write('Error')
                
                
if __name__ == '__main__':
       server_class = BaseHTTPServer.HTTPServer
       httpd = server_class(('',PORT_NUMBER), myHandler)
       try:
           httpd.serve_forever()
       except KeyboardInterrupt:
           pass
       httpd.server_close()

                

