#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time
import json
import urlparse
import sys
import urllib
import string
import math

from google.appengine.api import memcache
from google.appengine.api import users

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

def fetchdetails(self,nam,zipcode,response):

  try:  #self.response.write('hi')
    count=1
    songlst=[]
    r=urllib.urlopen('http://developer.echonest.com/api/v4/artist/profile?api_key=OQWYYBIAMT08XEK1J&name='+nam+'&bucket=genre&bucket=songs&bucket=hotttnesss&bucket=id:songkick&format=json').read()
    r=json.loads(r)
    artistorgid=str(r["response"]['artist']["id"])
    
    r2=urllib.urlopen('http://developer.echonest.com/api/v4/artist/video?api_key=OQWYYBIAMT08XEK1J&id='+artistorgid+'&format=json&results=1&start=0').read()
    r2=json.loads(r2)
    #print r2
    #self.response.write(r)
    for j1 in r2['response']['video']:
        videourl=j1['url']
        songurl=j1['image_url']
        #print(songurl)
        #response+="<iframe width="+str(420)+"height="+str(315)+"src="+songurl+"></iframe>"
        response+="<br><a href="+videourl+"><img src="+songurl+" alt=Music style=width:304px;height:228px;border:0></a>"
        response+="<p>Click Image to view Artist's most popular Video Song</p>"
        
        #response+="<img src="+songurl+" alt=Music style=width:304px;height:228px>"
    for j in r['response']['artist']['foreign_ids']:
        artistid=j['foreign_id']
    
    artistid=string.split(artistid,":")
    artist=artistid[2]
    print artist
    #self.response.write("Artist :"+r["response"]['artist']["name"]+'\n')
    response+= "<p><br><br>Artist Name : <tt>%s</tt></p>" % ( str(r["response"]['artist']["name"]) )
    #self.response.write("Popularity :"+str(r["response"]['artist']["hotttnesss"])+'\n')
    #self.response.write(artist)
    
    
    response+= "<p>Artist Popularity Index : <tt>%s</tt></p>" % ( str(r["response"]['artist']["hotttnesss"]) )
    #self.response.write('Top Songs of the artist: \n')
    response+= "<p><br><br>Top Songs of the artist : </p>"
    for i in r["response"]['artist']["songs"]:
        if i["title"].lower() not in songlst:
            #self.response.write(str(count)+' : '+i["title"]+'\n')
            response+= "<p> \t -o- %s</p>" % (i["title"] )
            songlst.append(i["title"].lower())
            count =count+1
    #self.response.write('\n\n')
    
    if artist is None:
        response+='<p>Error... artist name missing</p>'
    return artist,response
  except:
     artist =None
     response+='<p>Error... artist name missing in database</p>'
     return artist,response

def fetchevent(self,nam,zipcode,arid,response):
    eventname=[]
    eventloc=[]
    eventdis=[]
    eventtime=[]
    r1=urllib.urlopen('http://api.songkick.com/api/3.0/artists/'+str(arid)+'/calendar.json?apikey=X16HfvTA28vSWIex')
    r3=r1.read()
    r3=json.loads(r3)
    
    #json_string = json.dumps(r2,sort_keys=True,indent=2)
    #events=r2["event"]
    zi=urllib.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+str(zipcode)+'&sensor=false').read()
    zi=json.loads(zi)
    #self.response.write(zi["results"])
    for i in zi["results"]:
        #self.response.write(i['geometry'])
        lat1=i['geometry']["location"]["lat"]
        long1=i['geometry']["location"]["lng"]
    try:
     maplocations=""
     for item in r3["resultsPage"]["results"]["event"]:
      try:
    
        #self.response.write(item['location']['city']+'\n')
        lat2=item['location']["lat"]
        long2=item['location']["lng"]
        maplocations+= str(lat2)+","+str(long2)+'|'
        #print maplocations
       # self.response.write(str(lat2)+'\n')
        #self.response.write(str(long2)+'\n')
        dist=distance_on_unit_sphere(lat1, long1, lat2, long2)
        #self.response.write(str(dist)+'\n')
        eventdis.append(dist)
        eventname.append(item['displayName'])
        eventloc.append(item['location']['city'])
        eventtime.append(item['start']['datetime'])
      except:
        continue
    #except:
     # response+=('<This artist has no future events !!>')
     #sys.exit()
    #print maplocations
     op=min(eventdis,key=float)
     index1=eventdis.index(op)
     evname=eventname[index1]
     evloc=eventloc[index1]
     try:
      evtime=string.split(eventtime[index1],'T')
      response+= "<p><br><br>Date of Nearest Event : <tt>%s</tt></p>" % (str(evtime[0]))
    #self.response.write('time '+str(evtime[1])+'\n')
      response+= "<p>Time of Nearest Event : <tt>%s</tt></p>" % (str(evtime[1]))
     except:
      response+= "<p>Time: To be announced</p>"
      
    #self.response.write('Nearest Event to the given zipcode Name :'+evname+'\n')
     response+= "<p>Nearest Event to the your zipcode : <tt>%s</tt></p>" % (evname)
    #self.response.write('Date : '+str(evtime[0])+'\n')
    
    #self.response.write(evloc+'\n')
     response+= "<p>City of Nearest Event : <tt>%s</tt></p>" % (evloc)
    #self.response.write(str(op)+' miles'+'\n')
     response+= "<p>No. of Miles from you : <tt>%s</tt></p>" % (str(op))
     resp="https://maps.googleapis.com/maps/api/staticmap?size=400x400&markers=color:blue%7Clabel:"+maplocations
     print resp
     response+="<br><br><br><img src="+resp+"alt=Maps style=width:400px;height:400px>"
     response+= "<p>Artist's Concert Tour Map showing all concert locations</p>"
    except:
      response+='<p>This artist has no future events!</p>'
    if eventname is []:
        return 0,response
        
    else :return 1,response



class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        self.response.write("<h1 align='center'> MUZE : Your Music Inquirer Service</h1>")
        
        artname = None
        if 'artname' in self.request.GET.keys():
          artname = self.request.GET['artname']
        zipcode = None
        if 'zipcode' in self.request.GET.keys():
          zipcode = self.request.GET['zipcode']
          
        if 'reset' in self.request.GET.keys():
          memcache.flush_all()

        response=""
        
        if artname != None and zipcode!=None:
          
         arid,response=fetchdetails(self,artname,zipcode,response)
         if arid != None:

                #self.response.write(r)
          r1,response=fetchevent(self,artname,zipcode,arid,response)
          if r1 is 0:
                  self.response.write('<No events found!>')
                    #sys.exit()
          

          if not memcache.get("total"):
              memcache.set(key="total",value=1)
              totvalue=1
          else : 
              totvalue=int(memcache.get("total"))+1
              #print str(artvalue)
              memcache.set(key="total",value=totvalue)
          response+="<p><br><br><br>Total views for this site :<tt>%s</tt></p>" % (str(totvalue))

            #except ArithmeticError:
          if not memcache.get(artname):
              memcache.set(key=artname,value=1)
              artvalue=1
             # print int(artvalue) # So they can't revote
         # memcache.incr(artname+self.request.GET['answer'], initial_value=0)
          
          else: 
              artvalue=int(memcache.get(artname))+1
              #print str(artvalue)
              memcache.set(key=artname,value=artvalue)
          response+="<p>Total views for this artist :<tt>%s</tt></p>" % (str(artvalue))
         self.response.write(response)
         # print str(artvalue)
          #self.response.write('<Current views for this artist :"%s">' % str(artvalue))
          
        
        else:
        #for r in range():
         #   self.response.write(str(r) + ':' + str(memcache.get(artname+str(r))))
          #  self.response.write('<br>')
          self.response.write('<form name="input" method="get" action="/"><br>Enter Artist name:<input name="artname" type="text" value="%s">' % artname)
          self.response.write('<br><form name="input" method="get" action="/"><br>Enter Zipcode<input name="zipcode" type="text" value="%s">' % zipcode)
          self.response.write('<br><br><br><input type="submit" value="Submit"> </form><br>')

          self.response.write('<br><br><br><br><br><br><br><br><form name="input" method="get" action="/"><input name="reset" type="hidden" value="1"><input type="submit" value="Flush Memcache"> </form>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
