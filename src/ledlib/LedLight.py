#!/usr/bin/env python

import socket
import binascii
import time


# Base class for all led lights
# 
class LedLight:
  factor = 256.0 / 100

  def __init__(self, name, ipAddrOrName = None, ipPort = None):
    self.connected = False
    self.name = name

    if ipAddrOrName is None:
      ipAddrOrName = name

    if ipPort is None:
      ipPort = 5577

    self.ipAddr = socket.gethostbyname(ipAddrOrName)
    self.ipPort = ipPort
    self.openSocket()

  # Scale the value from 0-99 to 0-255
  def scale(self, val):
    return max(min(255, int(val*self.factor)), 0)

  def openSocket(self):
    try:
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.connect((self.ipAddr, self.ipPort))
      self.connected = True
    except socket.error, exc:
      print "Caught exception socket.error : %s" % exc

  # takes a list of bytes
  def echoAsHex(self,bin_list):
    hexStr = binascii.hexlify(bytearray(bin_list))
    print 'hex string: '+hexStr

  # Convert a list of bytes to a binary string
  def convertToBin(self,byte_list):
    str = ""
    for i in byte_list:
        str += chr(i)

    return str

  # Transmit a binary message
  def xmit(self,bin_msg):
    if self.connected:
      try:
        self.s.send(bin_msg)
      except:
        print "Exception sending message"

    else:
      print self.name+" is not connected"

  # Transmit a binary message
  def recv(self,bin_msg, msg_len, timeout=1):
    self.xmit(bin_msg)
    
    if self.connected:
      chunks = []
      bytes_recd = 0
      while bytes_recd < msg_len:
        chunk = self.s.recv(min(msg_len - bytes_recd, 2048))
        if chunk == '':
          raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
      return ''.join(chunks)
    else:
      print "Not connected"

  # Send an RGB message
  def sendRGB(self,red, green, blue):
    pass
        
  # Send a white message    
  def sendWhite(self, white):
    pass

  def turnOff(self):
    pass

  def turnOn(self):
    pass

  def isOn(self):
    pass

  def getWhite(self):
    pass

  def getRGB(self):
    pass

  def testX(self,data):
    data = self.addChkSum(data)
    self.echoAsHex(data)
    data = self.xmitrecv( self.convertToBin(data))
    if data != None:
      print "Data returned: "+binascii.hexlify(data)
    else:
      print "No data returned"
    time.sleep(1)
