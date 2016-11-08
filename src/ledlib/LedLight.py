#!/usr/bin/env python

import socket
import binascii
import time


# Base class for all led lights
# 
class LedLight:
  def __init__(self, name, ipAddrOrName = None, ipPort = None):
    self.name = name

    if ipAddrOrName is None:
      ipAddrOrName = name

    if ipPort is None:
      ipPort = 5577

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
  def xmitrecv(self,bin_msg,timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.settimeout(2.0)
    s.connect((self.ipAddr, self.ipPort))
    s.send(bin_msg)
    s.setblocking(0)

    chunks = []
    begin = time.time()
    while 1:
      if chunks and time.time() - begin > timeout:
        break
      elif time.time() - begin > timeout * 2:
        break
      try:
        chunk = s.recv(8192)
        if chunk:
          chunks.append(chunk)
          begin = time.time()
        else:
          time.sleep(0.1)
      except:
        pass

    s.close()
    return ''.join(chunks)

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
 
