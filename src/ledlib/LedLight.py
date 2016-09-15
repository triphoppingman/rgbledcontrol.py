#!/usr/bin/env python

import socket
import binascii
import time


# Base class for all led lights
# 
class LedLight:
  def __init__(self, name, ipAddrOrName, ipPort):
    self.name = name
    self.ipAddr = socket.gethostbyname(ipAddrOrName)
    self.ipPort = ipPort
        
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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.connect((self.ipAddr, self.ipPort))
    s.send(bin_msg)
    s.close()
    return None 

  # Transmit a binary message
  def xmitrecv(self,bin_msg):
    data = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.settimeout(2.0)
    s.connect((self.ipAddr, self.ipPort))
    s.send(bin_msg)
    try:
        data = s.recv(1024)
    except socket.timeout:
        print "timed out"

    s.close()
    return data 

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

  def testX(self,data):
    data = self.addChkSum(data)
    self.echoAsHex(data)
    data = self.xmitrecv( self.convertToBin(data))
    if data != None:
      print "Data returned: "+binascii.hexlify(data)
    else:
      print "No data returned"
    time.sleep(1)

  def testYr(data):
    self.echoAsHex(data)
    self.data = xmitrecv( self.convertToBin(data))
    if data != None:
      print "Data returned: "+binascii.hexlify(data)
    else:
      print "No data returned"    
    time.sleep(1)

  def testY(data):
    echoAsHex(data)
    data = xmit( convertToBin(data))
    time.sleep(1)
 
