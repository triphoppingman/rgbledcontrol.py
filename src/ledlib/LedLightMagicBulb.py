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

    chksum &= 255
    bin_list.append(chksum)
    return bin_list

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    return self.sendRGBHex(red*self.factor, green*self.factor, blue*self.factor)

  # Send an RGB message (and each color element is in range 0-255)
  def sendRGBHex(self,red, green, blue):
    return self.xmit(self.convertToBin(self.addChkSum([49,red, green, blue, 0, 240, 15])))

  # Send a white message    
  def sendWhite(self, white):
    return self.sendWhiteHex(white*self.factor)

  # Send a white message (the white value is a 0-255)
  def sendWhiteHex(self, white):
    return self.xmit(self.convertToBin(self.addChkSum([49,0, 0, 0, white, 15, 15])))

  def turnOff(self):
    return self.xmit(self.convertToBin(self.addChkSum([113,36,15])))

  def turnOn(self):
    return self.xmit(self.convertToBin(self.addChkSum([113,35,15])))

  def isOn(self):
    data = self.xmitrecv( self.convertToBin(self.addChkSum([129,138,139])))
    if data and len(data)>2:
      return binascii.hexlify(data[2]) == '23'
    else:
      return 0


  def getWhite(self):
    data = self.xmitrecv(self.convertToBin(self.addChkSum([129, 138, 139])))
    if data and len(data) > 8:
      return ord(data[9])
    else:
      return -1


  def getRGB(self):
    data = self.xmitrecv(self.convertToBin(self.addChkSum([129, 138, 139])))
    if data and len(data) > 8:
      red = ord(data[6])
      green = ord(data[7])
      blue = ord(data[8])
      return [red, green, blue]
    else:
      return -1



