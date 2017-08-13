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
    try:
      self.bulb.set_name(name)
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    try:
      self.bulb.set_rgb(red, green, blue)
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  # Send a white message    
  def sendWhite(self, white):
    try:
      self.bulb.set_color_temp(5000)
      self.bulb.set_brightness(white)
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def turnOff(self):
    try:
      return self.bulb.turn_off()
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc


  def turnOn(self):
    try:
      self.bulb.turn_on()
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def isOn(self):
    try:
      return self.bulb.get_properties()['power'] == 'on'
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def getWhite(self):
    try:
      properties = self.bulb.get_properties()
      if(properties['color_mode']=='2'):
        return int(properties['bright'])
      else:
        return -1
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def getRGB(self):
    try:
      properties = self.bulb.get_properties()
      if(properties['color_mode']=='1'):
        rgb = int(properties['rgb'])
        return [(rgb >> 16) & 255, (rgb >> 8) & 255, rgb & 255]
      else:
        return -1
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

