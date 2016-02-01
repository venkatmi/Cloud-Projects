import rpyc


''' Class to store all external function calls
'''
class Service(rpyc.Service):
  def on_connect(self):
    pass

  def on_disconnect(self):
    print "Someone left!"

  def exposed_setCallback(self,showMe):
    c.setCallback(showMe)

  def exposed_setCallback1(self,fileShared):
    c.setCallback1(fileShared)
    
  def exposed_setCallback2(self,sendFile):
    c.setCallback2(sendFile)

  def exposed_say(self, message):
    c.say(message)
    
  def exposed_app(self,foldername):
    c.app(foldername)
    
  def exposed_filapp(self,filname,name):
    c.filapp(filname,name)
    
  def exposed_show(self):
    c.show()
 
  def exposed_fetch(self,filename):
    c.fetch(filename)
    
  

''' A chat server class
  This stores a single state for all the clients
  in the self.callbacks private variable
'''
class ChatServer:
  def __init__(self):
    self.callbacks = []
    self.foldname=[]
    self.fname=dict()
    self.callbacks1=[]
    self.callbacks2=[]
  # Append the function call (remote) to the list of clients
  def setCallback(self, showMe):
    self.callbacks = self.callbacks + [showMe]
    
  def setCallback1(self,fileShared):
    self.callbacks1 = self.callbacks1 + [fileShared]
    
  def setCallback2(self,sendFile):
    self.callbacks2 = self.callbacks2 + [sendFile]

  # Send that message to everyone's showMe method
  def say(self, message):
    for fn in self.callbacks:
      try:  # Put in a try/except block just in case we lost net connection
        fn(message)
      except:
        pass
    
  def app(self,foldername):
    if foldername not in self.foldname:
        self.foldname.append(foldername)
    
  def filapp(self,filname,name):
    if filname not in self.fname:
       # print filname,name
        self.fname[filname]=name
        
  def show(self):
    for fn in self.callbacks1:
      try:
        # Put in a try/except block just in case we lost net connection
        for i in self.foldname:
            print i 
            fn(i)
      except:
        pass
    
  def fetch(self,filename):
    for fn in self.callbacks2:
        try:
            name1=self.fname[filename]
            print name1,filename
            fn(filename,name1)
        except:
            pass
            
  
if __name__ == "__main__":
  from rpyc.utils.server import ThreadedServer
  c = ChatServer()
  t = ThreadedServer(Service, port = 18861)
  t.start()#!/usr/bin/env python

