# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 28, 2015 2:27:22 PM$"

from ServerCommand import ServerCommand

class LedLightCommandHandler:
  def __init__(self, objset = []):
    self.objdict = { obj.name:obj for obj in objset }
  
  def handleCommand(self, command):
    for objname in command.objects:
      if(objname in self.objdict):
        objref = self.objdict[objname]
        methargs = dict() #{"self":objref}
        methargs.update(command.kvdict)
        getattr(objref, command.comname)(**methargs)
      else:
        print "Object: "+obj+ " not defined"
      
    return 0

if __name__ == "__main__":
  print "Hello World"
  
  
