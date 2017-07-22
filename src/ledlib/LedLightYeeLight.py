#!/usr/bin/env python
from yeelight import Bulb

from LedLight import LedLight


# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightYeeLight(LedLight):
  def __init__(self, name, ipAddrOrName=None):
    if ipAddrOrName is None:
      ipAddrOrName = name

    self.bulb = Bulb(ipAddrOrName)
    self.bulb.set_name(name)

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    return self.bulb.set_rgb(red, green, blue)

  # Send a white message    
  def sendWhite(self, white):
    self.bulb.set_color_temp(5000)
    self.bulb.set_brightness(white)

  def turnOff(self):
    return self.bulb.turn_off()

  def turnOn(self):
    return self.bulb.turn_on()

