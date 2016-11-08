#!/usr/bin/env python

import time
from ledlib.LedLightMagicBulb import LedLightMagicBulb
from ledlib.LedLightWifi370 import LedLightWifi370



 
#a1 = LedLight('192.168.1.251',5577,1)
#a2 = LedLight('192.168.1.217',5577,2)
#a1.turnOn()
#a2.turnOn()
#time.sleep(1)
#a1.sendWhite(10)
#a2.sendWhite(10)
#time.sleep(1)
#a1.sendWhite(200)
#a2.sendWhite(200)
#time.sleep(1)
#a1.sendWhite(10)
#a2.sendWhite(10)
#time.sleep(1)
#a1.sendWhite(200)
#a2.sendWhite(200)
#time.sleep(1)
#a1.sendWhite(10)
#a2.sendWhite(10)
#time.sleep(1)
#a1.sendWhite(200)
#a2.sendWhite(200)
#time.sleep(1)
#a1.turnOff()
#a2.turnOff()

#a1.turnOn()
#a1.turnOn()

a3 = LedLightMagicBulb('bulb06')
#a3.turnOff()
#time.sleep(1)
#a3.testX([129,138,139])
#print a3.isOn()
#time.sleep(1)
#a3.turnOn()
#time.sleep(2)
#a3.testX([129,138,139])
print a3.isOn()
# time.sleep(1)
# a3.sendWhiteHex(127)
# time.sleep(.1)
#
# print a3.getWhite()
# a3.testX([129,138,139])
# time.sleep(.1)
# a3.sendWhiteHex(255)
# time.sleep(1)
# print a3.getWhite()
# time.sleep(1)
# a3.testX([129,138,139])
# time.sleep(1)
a3.sendRGBHex(255,0,0)
time.sleep(.5)
print a3.getRGB()
time.sleep(.5)
a3.sendRGBHex(0,255,0)
time.sleep(.5)
print a3.getRGB()
time.sleep(.5)
a3.sendRGBHex(0,0,255)
time.sleep(.5)
print a3.getRGB()
# time.sleep(1)

#while 1:
#	a3.sendRGBHex(255,255,255)
#	time.sleep(.1)
#	a3.sendRGBHex(255,0  ,0  )
#	time.sleep(.1)
#	a3.sendRGBHex(0  ,255,0  )
#	time.sleep(.1)
#	a3.sendRGBHex(0  ,0  ,255)
#	time.sleep(.1)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(255,0  ,0  )
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(255,0  ,0  )
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(255,0  ,0  )
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(255,0  ,0  )
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(255,0  ,0  )
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)
	# a3.sendRGBHex(255,255,255)
	# a3.sendRGBHex(0  ,0  ,255)

#a1.turnOff()
#a1.testX([0x81, 0x8a, 0x8b])
#for x in range(10,200):
#    sendRGB(0,x,0)

#sendRGB(255,0,0)
#time.sleep(1)
#sendRGB(0,255,0)
#time.sleep(1)
#sendRGB(0,0, 255)
#time.sleep(1)
#sendRGB(0,0,0)

#testX([-127,-118,-117])
#testX([49,100,0,0,0,0,0,-16])
#testX([49,0,0,0,100,200,-16,15])
#testX([97,10,10,-16])
#testX([17,26,27,15]) -- does nothing
#testX([113,35,-16]) -- does nothing
#testX([113,36,-16]) -- does nothing
#testX([113,35,15]) # Fade in
#testX([113,36,15]) # Fade out
#time.sleep(5)
#testX([113,35,15]) # Fade in
#testX([34,42,43,15]) - nothing
#testX([34,42,43,15]) - nothing

#sendWhite(128)
#time.sleep(1)
#fadeOut()
#time.sleep(1)
#sendRGB(0,255,0)
#time.sleep(1)
#fadeIn()
#time.sleep(1)
#turnOff()


#testYr([0xEF,0x01,0x77])

#testY([0xCC, 0x24,0x33]) # Turn turnOff

#testY([0xCC, 0x23,0x33]) # Turn turnOff

#testY([0xBB, 0x25, 0x10, 0x44])

