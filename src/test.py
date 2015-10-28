#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:02:18 PM$"

from ledlib.LedLightMagicBulb import LedLightMagicBulb
import time

if __name__ == "__main__":
  print "Hello World";

  a1 = LedLightMagicBulb('192.168.1.29', 5577)
  a1.turnOn()
  time.sleep(1)
  a1.sendWhite(100)
  time.sleep(1)
  a1.sendRGB(50,20,0)
  time.sleep(1)
  a1.turnOff()
