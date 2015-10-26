# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:09:55 PM$"


from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from ServerCommand import ServerCommand

class LedLightProtocol(LineReceiver):
  delimiter = '\n'
  def lineReceived(self, line):
    command = ServerCommand(line)
    if hasattr(command, 'errmsg'):
      self.sendLine("nok:"+command.errmsg)
    else:
      self.sendLine("ok")

class LedLightFactory(ServerFactory):
    # This will be used by the default buildProtocol to create new protocols:
    protocol = LedLightProtocol

if __name__ == "__main__":
  print "Running now"
  reactor.listenTCP(8123, LedLightFactory())
  reactor.run()