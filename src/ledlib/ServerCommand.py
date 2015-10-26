# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 21, 2015 3:03:57 PM$"

from pyparsing import Word, alphas, alphanums, delimitedList, quotedString, Group,ParseException
from pprint import pprint

#define the grammar
# The objects
OBJECT = Word(alphas, alphanums+'_')
OBJECTS = delimitedList(OBJECT('object'))
OBJLIST = '{' + OBJECTS('objects') + '}'

#The arguments 
KEY = Word(alphas)
VALUE = quotedString()
KVPAIR = Group(KEY('key')+'='+VALUE('value'))
KVPAIRS = delimitedList(KVPAIR('kvpair'))
KVLIST = '(' + KVPAIRS('kvpairs') + ')'

# The command
COMNAME = Word(alphas)
COMMAND = OBJLIST('objlist') + COMNAME('comname') + KVLIST('kvlist')
COMSPEC = COMMAND('command')

class ServerCommand:
  def __init__(self, commandLine):
    self.commandLine = commandLine
    try:
      fn = COMSPEC.parseString(commandLine)
      self.comname = fn.comname
      self.objects = fn.objects
      self.kvpairs = fn.kvpairs
    except Exception as e:
      self.errmsg = str(e)

if __name__ == "__main__":
  serverCmd1 = ServerCommand("{A,B,C}command(D='E', F='G')")
  print "command = "+serverCmd1.comname
  for obj in serverCmd1.objects:
    print "Object: "+obj
  for kvpair in serverCmd1.kvpairs:
    print "Argument key: "+kvpair.key+" = "+kvpair.value
