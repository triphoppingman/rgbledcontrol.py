# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 21, 2015 10:35:22 AM$"

from pyparsing import Word, alphas, alphanums, delimitedList, quotedString, Group
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

if __name__ == "__main__":
  print "testing1"
  for fn,s,e in OBJLIST.scanString("{h,k}"):
    for obj in fn.objects:
      print "Object: "+obj
      
  print "testing2"
  for fn,s,e in KVLIST.scanString("(P='Q',R='s')"):
    for kvpair in fn.kvpairs:
      print "Argument key: "+kvpair.key+" = "+kvpair.value
    
  print "testing3"
  for fn,s,e in COMSPEC.scanString("{A,B,C}commandAA(D='E', F='G')"):
    print "command = "+fn.comname
    for obj in fn.objects:
      print "Object: "+obj
    for kvpair in fn.kvpairs:
      print "Argument key: "+kvpair.key+" = "+kvpair.value
