#!/usr/bin/env python

from LedLight import LedLight


# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
#
COLOR_FACTOR = 0.8

class LedLightWifi370(LedLight):

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    return self.xmit(self.convertToBin([0x56,self.scale(red), self.scale(green), self.scale(blue), 0xAA]))

  # Send a white message    
  def sendWhite(self, white):
    return self.sendRGB(white, white, int(white * COLOR_FACTOR))

  def turnOff(self):
    return self.xmit(self.convertToBin([0xCC, 0x24,0x33]))

  def turnOn(self):
    return self.xmit(self.convertToBin([0xCC, 0x23,0x33]))

  def isOn(self):
    data = self.recv(self.convertToBin([0xEF, 0x01, 0x77]),11)
    if data and len(data)>2:
      return ord(data[2]) == 0x23
    else:
      return 0

  def getWhite(self):
    pass

  def getRGB(self):
    data = self.recv(self.convertToBin([0xEF, 0x01, 0x77]),11)
    if data and len(data)>2:
      return [(ord(data[6])), (ord(data[7])), (ord(data[8]))]
    else:
      return 0