#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.ledlib.LedLightYeeLight import LedLightYeeLight

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:02:18 PM$"

from ledlib.LedLightYeeLight import LedLightYeeLight
from ledlib.LedLightHueLight import LedLightHueLight
from ledlib.LedLightMagicBulb import LedLightMagicBulb
from ledlib.LedLightMagicBulb import LedLightMagicBulb
from ledlib.LedLightWifi370 import LedLightWifi370
from ledlib.LedLightGroup import LedLightGroup
from ledlib.LedLightCommandHandler import LedLightCommandHandler
from ledlib.ServerCommand import ServerCommand

import time

if __name__ == "__main__":
  print "Hello World";

  #a1 = LedLightMagicBulb('a1', '192.168.1.29', 5577)
  # a2 = LedLightMagicBulb('bulb0')
##  a3 = LedLightWifi370('a3', 'strip05', 5577)

  # a4 = LedLightYeeLight('bulb08')
  # a4.turnOff()
  # time.sleep(1)
  # a4.turnOn()
  # time.sleep(1)
  # a4.turnOff()
  # time.sleep(1)
  # a4.turnOn()
  # time.sleep(1)
  # a4.sendWhite(100)
  # time.sleep(1)
  # a4.sendWhite(75)
  # time.sleep(1)
  # a4.sendWhite(50)
  # time.sleep(1)
  # a4.sendWhite(25)
  # time.sleep(1)
  # a4.sendRGB(25, 45, 65)
  # time.sleep(1)
  # a4.sendRGB(45, 65, 25)
  # time.sleep(1)
  # a4.sendRGB(65, 25, 45)
##  a1.turnOn()
#  time.sleep(1)
#  a1.sendWhite(100)
#  time.sleep(1)
#  a1.sendRGB(50,20,0)
#  time.sleep(1)
#  a1.turnOff()

#   g1 = LedLightGroup('g1', [a2])
# #  g1.turnOn()
# #  while 1:
# #    g1.sendWhite(50)
# #    time.sleep(1)
# #    g1.sendRGB(100,0,0)
# #    time.sleep(1)
# #    g1.sendRGB(0,90,0)
# #    time.sleep(1)
# #    g1.sendRGB(0,0,70)
# #    time.sleep(1)
# #  g1.turnOff()
#   handler = LedLightCommandHandler([g1])
#  handler.handleCommand(ServerCommand("{g1}turnOn"))
#  time.sleep(2)
#  handler.handleCommand(ServerCommand("{g1}turnOff"))
#  time.sleep(2)
#  handler.handleCommand(ServerCommand("{g1}turnOn"))
#  time.sleep(2)
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

  # redOn = ServerCommand("{g1}sendRGB(red=100,blue=0,green=0)")
  # whiteOn = ServerCommand("{g1}sendRGB(red=100,blue=100,green=100)")
  # blueOn = ServerCommand("{g1}sendRGB(red=0,blue=100,green=0)")
  #
  # while 1:
  #   g1.sendWhite(75)
  #   time.sleep(0.5)
  #   g1.sendWhite(15)
  #   time.sleep(0.5)


#  for i in range(100):
#    for j in range(5):
#      handler.handleCommand(redOn)
#      handler.handleCommand(whiteOn)
#    for j in range(5):
#      handler.handleCommand(blueOn)
#admin      handler.handleCommand(whiteOn)

  # a4 = LedLightYeeLight('bulb08')
  # a4.turnOn()
  # time.sleep(.5)
  # # print a4.isOn()
  # # a4.turnOff()
  # # time.sleep(.5)
  # # print a4.isOn()
  # # a4.turnOff()
  # # time.sleep(.5)
  # # print a4.isOn()
  # a4.sendWhite(2)
  # time.sleep(.5)
  # print a4.getWhite()
  # a4.sendWhite(50)
  # time.sleep(.5)
  # print a4.getWhite()
  # a4.sendWhite(100)
  # time.sleep(.5)
  # print a4.getWhite()
  # a4.sendRGB(100,0,0)
  # time.sleep(.5)
  # print a4.getRGB()
  # a4.sendRGB(0,100,0)
  # time.sleep(.5)
  # print a4.getRGB()
  # a4.sendRGB(0,0,100)
  # time.sleep(.5)
  # print a4.getRGB()

a6 = LedLightHueLight('192.168.1.50', 'Hue color lamp 4')
print a6.isOn()
time.sleep(1)
a6.turnOff()
print a6.isOn()
time.sleep(1)
a6.turnOn()
time.sleep(1)
a6.sendRGB(100, 0, 0)
print a6.getRGB()
time.sleep(.5)
a6.sendRGB(0, 100, 0)
print a6.getRGB()
time.sleep(.5)
a6.sendRGB(0, 0, 100)
print a6.getRGB()
time.sleep(.5)
a6.sendWhite(250)
time.sleep(1)
print a6.getWhite()

