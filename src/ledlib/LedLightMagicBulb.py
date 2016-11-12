#!/usr/bin/env python

from LedLight import LedLight
import binascii

# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightMagicBulb(LedLight):
  factor = 256/100
  
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
    return self.sendRGBHex(red*self.factor, green*self.factor, blue*self.factor)

  # Send an RGB message (and each color element is in range 0-255)
  def sendRGBHex(self,red, green, blue):
    return self.xmit(self.convertToBin(self.addChkSum([0x31,red, green, blue, 0, 0xf0, 0x0f])))

  # Send a white message    
  def sendWhite(self, white):
    return self.sendWhiteHex(white*self.factor)

  # Send a white message (the white value is a 0-255)
  def sendWhiteHex(self, white):
    return self.xmit(self.convertToBin(self.addChkSum([0x31,0, 0, 0, white, 0x0f, 0x0f])))

  def turnOff(self):
    return self.xmit(self.convertToBin(self.addChkSum([0x71, 0x24, 0x0f])))

  def turnOn(self):
    return self.xmit(self.convertToBin(self.addChkSum([0x71, 0x23, 0x0f])))

  def isOn(self):
    self.xmit( self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])))
    data = self.recv()
    if data and len(data)>2:
      return binascii.hexlify(data[2]) == '23'
    else:
      return 0


  def getWhite(self):
    self.xmit( self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])))
    data = self.recv()
    if data and len(data) > 8:
      return ord(data[9])
    else:
      return -1


  def getRGB(self):
    self.xmit( self.convertToBin(self.addChkSum([0x81, 0x8a, 0x8b])))
    data = self.recv()
    if data and len(data) > 8:
      red = ord(data[6])
      green = ord(data[7])
      blue = ord(data[8])
      return [red, green, blue]
    else:
      return -1



