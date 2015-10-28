#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:02:18 PM$"

from ledlib.LedLightMagicBulb import LedLightMagicBulb
from ledlib.LedLightWifi370 import LedLightWifi370
from ledlib.LedLightGroup import LedLightGroup
from ledlib.LedLightCommandHandler import LedLightCommandHandler
from ledlib.ServerCommand import ServerCommand

import time

if __name__ == "__main__":
  print "Hello World";

  a1 = LedLightMagicBulb('a1', '192.168.1.29', 5577)
  a2 = LedLightMagicBulb('a2', '192.168.1.251', 5577)
  a3 = LedLightWifi370('a3', '192.168.1.217', 5577)
##  a1.turnOn()
#  time.sleep(1)
#  a1.sendWhite(100)
#  time.sleep(1)
#  a1.sendRGB(50,20,0)
#  time.sleep(1)
#  a1.turnOff()

  g1 = LedLightGroup('g1', [a1,a2,a3])
#  g1.turnOn()
#  while 1:
#    g1.sendWhite(50)
#    time.sleep(1)
#    g1.sendRGB(100,0,0)
#    time.sleep(1)
#    g1.sendRGB(0,90,0)
#    time.sleep(1)
#    g1.sendRGB(0,0,70)
#    time.sleep(1)
#  g1.turnOff()
  handler = LedLightCommandHandler([g1])
  handler.handleCommand(ServerCommand("{g1}turnOn"))
  time.sleep(1)
#  handler.handleCommand(ServerCommand("{g1}sendWhite(white=10)"))
#  time.sleep(1)
#  handler.handleCommand(ServerCommand("{g1}sendWhite(white=70)"))
#  time.sleep(1)
#  for i in range(10):
#    handler.handleCommand(ServerCommand("{g1}sendRGB(red=100,blue=0,green=0)"))
#    time.sleep(1)
#    handler.handleCommand(ServerCommand("{g1}sendRGB(red=0,blue=100,green=0)"))
#    time.sleep(1)
#    handler.handleCommand(ServerCommand("{g1}sendRGB(red=0,blue=0,green=100)"))
#    time.sleep(1)
#  handler.handleCommand(ServerCommand("{g1}turnOff"))

  redOn = ServerCommand("{g1}sendRGB(red=100,blue=0,green=0)")
  whiteOn = ServerCommand("{g1}sendRGB(red=100,blue=100,green=100)")
  blueOn = ServerCommand("{g1}sendRGB(red=0,blue=100,green=0)")
  
  for i in range(100):
    for j in range(5):
      handler.handleCommand(redOn)
      handler.handleCommand(whiteOn)
    for j in range(5):
      handler.handleCommand(blueOn)
      handler.handleCommand(whiteOn)

