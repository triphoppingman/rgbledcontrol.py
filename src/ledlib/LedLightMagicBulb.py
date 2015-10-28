#!/usr/bin/env python

from LedLight import LedLight

# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightMagicBulb(LedLight):
  factor = 255/100
  
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
    return self.xmit(self.convertToBin(self.addChkSum([49,red*self.factor, green*self.factor, blue*self.factor, 0, 240, 15])))

  # Send a white message    
  def sendWhite(self, white):
    return self.xmit(self.convertToBin(self.addChkSum([49,0, 0, 0, white*self.factor, 15, 15])))

  def turnOff(self):
    return self.xmit(self.convertToBin(self.addChkSum([113,36,15])))

  def turnOn(self):
    return self.xmit(self.convertToBin(self.addChkSum([113,35,15])))

