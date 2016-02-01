import rpyc
import os

def showMe(message):
  print "->", message
  
def fileShared(folder):
    #print folder,foldername
    if foldername == folder:
        filedet=os.listdir(foldername)
        #c.root.say(name+":")
        
        for i in filedet:
            c.root.say(i)
            #print i 
            c.root.filapp(i,name)

def sendFile(filename,name1):
    #print name,name1
    if name==name1:
        print(name+foldername+filename+"hurray")
        
  


c = rpyc.connect("localhost", 18861)
foldername=None
# In order to print the messages from others while the client thread
# is waiting for keyboard input, start up a background listening thread.
bgsrv = rpyc.BgServingThread(c)

name = raw_input("Enter Your Name:")





# Send the function to print a message to my screen to the server
c.root.setCallback(showMe)
c.root.setCallback1(fileShared)
c.root.setCallback2(sendFile)


while True:
   
  msg = raw_input()
  
  if '#' == msg:
    c.root.show()
    Receive=raw_input("Do you want to Choose a file from the list ?(y/n)")
    
    if Receive=="y":
        filename=raw_input("Enter file name:")
        c.root.fetch(filename)
    
    
  elif msg =="Send File":
    Validate=raw_input("Do you want to Send a file?(y/n)")
    if Validate=="y":
   
          foldername=raw_input("Enter file path:")
          
  elif msg =="*":
    Valid=raw_input("Do you want to share a folder?(y/n)")
    if Valid=="y":
   
          foldername=raw_input("Enter folder path:")
          c.root.app(foldername)
   
  else:
      c.root.say(name + ":" + msg)
  
  

    
    
    
bgsrv.stop()
c.close()#!/usr/bin/env python

