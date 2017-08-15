#!/usr/bin/env python

from LedLight import LedLight
import binascii

# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightMagicBulb(LedLight):
  def addChkSum(self,bin_list):
    chksum = 0
    for idx,val in enumerate(bin_list):
      if val < 0:
        val = -val + 128
        bin_list[idx] = val

      chksum += val

    chksum &= 0xff
    bin_list.append(chksum)
    return bin_list

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    return self.sendRGBHex(self.scale(red), self.scale(green), self.scale(blue))

  # Send an RGB message (and each color element is in range 0-255)
  def sendRGBHex(self,red, green, blue):
    return self.xmit(self.convertToBin(self.addChkSum([0x31,red, green, blue, 0, 0xf0, 0x0f])))

  # Send a white message    
  def sendWhite(self, white):
    return self.sendWhiteHex(self.scale(white))

  # Send a white message (the white value is a 0-255)
  def sendWhiteHex(self, white):
    return self.xmit(self.convertToBin(self.addChkSum([0x31,0, 0, 0, white, 0x0f, 0x0f])))

  def turnOff(self):
    return self.xmit(self.convertToBin(self.addChkSum([0x71, 0x24, 0x0f])))

  def turnOn(self):
    return self.xmit(self.convertToBin(self.addChkSum([0x71, 0x23, 0x0f])))

  def isOn(self):
    data = self.recv(self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])),14)
    if data and len(data)>2:
      return ord(data[2]) == 0x23
    else:
      return 0

  # Get the white intensity
  def getWhite(self):
    data = self.recv( self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])),14)
    if data and len(data) > 10:
      return self.unscale(ord(data[9]))
    else:
      return -1

  def getRGB(self):
    data = self.recv( self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])),14)
    if data and len(data) > 8:
      return [self.unscale(ord(data[8])), self.unscale(ord(data[9])), self.unscale(ord(data[10]))]
    else:
      return -1



