# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 28, 2015 9:01:03 AM$"

class LedLightGroup:
  def __init__(self, name, members = []):
    self.name = name
    self.members = members

  def turnOn(self):
    for member in self.members:
      member.turnOn()
      
  def turnOff(self):
    for member in self.members:
      member.turnOff()
      
  def sendRGB(self, red, green, blue):
    for member in self.members:
      member.sendRGB(red, green, blue)
      
  def sendWhite(self, white):
    for member in self.members:
      member.sendWhite(white)
      
