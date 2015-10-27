# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:09:55 PM$"


from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from ServerCommand import ServerCommand

# Protocol for the led light
# Processes the line and if parses ok, hands off to command handler
class LedLightProtocol(LineReceiver):
  delimiter = '\n'
  def lineReceived(self, line):
    command = ServerCommand(line)
    if hasattr(command, 'errmsg'):
      self.sendLine("nok:"+command.errmsg)
    else:
      if self.commandHandler.handleCommand(command)==0:
        self.sendLine("ok")
      else: 
        self.sendLine("nok:"+self.commandHandler.errmgs)
        

# Hooks up the protocol to the server factory
class LedLightFactory(ServerFactory):
    def __init__(self, commandHandler):
      self.protocol = LedLightProtocol
      self.protocol.commandHandler = commandHandler

# Null command handler - does nothing really - just print the command
class NullCommandHandler:
  def handleCommand(self, command):
    print "Handling command: "+command.comname
    return 0

# This function does the deed - runs the server with the handler
def runServer(port, commandHandler):
  reactor.listenTCP(port, LedLightFactory(commandHandler))
  reactor.run()
  
if __name__ == "__main__":
  print "Running now"
  runServer(8123,NullCommandHandler())