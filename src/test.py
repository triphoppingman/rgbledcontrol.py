#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "bruce"
__date__ = "$Oct 11, 2015 4:02:18 PM$"

from ledlib.LedLight import LedLight


if __name__ == "__main__":
  print "Hello World";

  a1 = LedLightMagicBulb('192.168.1.29', 5577)
  a1.turnOn()
  a1.sendRGB(102,51,0)
