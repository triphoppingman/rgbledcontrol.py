#!/usr/bin/env python
from phue import Bridge

from LedLight import LedLight
from PhueConverter import Converter, GamutB


# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLightHueLight(LedLight):
  # All the bridges in the system (indexed by IP address)
  bridge = None

  # Name of the light, ip address of the bridge and the number of the light in the bridge
  def __init__(self, ipAddr, name, gamut=GamutB):

    # If we don't have a record of this bridge, add it
    if not self.bridge:
      self.bridge = Bridge(ipAddr)

    self.light = self.bridge.get_light_objects('name')[name]
    self.name = name
    self.converter = Converter(gamut)

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    try:
#      self.light.colormode = 'xy'
      self.light.xy = self.converter.rgb_to_xy(self.scale(red), self.scale(green), self.scale(blue))
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  # Send a white message    
  def sendWhite(self, white, temp = 350):
    try:
      self.light.colortemp = temp
      self.light.brightness = self.scale(white)
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def turnOff(self):
    try:
      self.light.on = False
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc


  def turnOn(self):
    try:
      self.light.on = True
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def isOn(self):
    try:
      return self.light.on
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

  def getWhite(self):
    try:
      if(self.light.colormode == 'ct'):
        return self.unscale(self.light.brightness)
      else:
        return -1
    except Exception as exc:
      print "Caught exception socket.error : %s" % exc

# comment
  def getRGB(self):
    (x,y) = self.light.xy
    (r,g,b) = self.converter.xy_to_rgb(x,y)
    return (self.unscale(r), self.unscale(g), self.unscale(b))

