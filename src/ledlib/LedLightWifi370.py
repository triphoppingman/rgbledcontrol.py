#!/usr/bin/env python

from LedLight import LedLight


# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightWifi370(LedLight):
  factor = 255/100
  
  # Send an RGB message
  def sendRGB(self,red, green, blue):
    return self.xmit(self.convertToBin([0x56,red*self.factor, green*self.factor, blue*self.factor, 0xAA]))

  # Send a white message    
  def sendWhite(self, white):
    white *= self.factor
    return self.sendRGB(white, white, white)

  def turnOff(self):
    return self.xmit(self.convertToBin([0xCC, 0x24,0x33]))

  def turnOn(self):
    return self.xmit(self.convertToBin([0xCC, 0x23,0x33]))

