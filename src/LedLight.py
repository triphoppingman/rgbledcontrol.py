#!/usr/bin/env python

import socket
import base64
import array
import binascii
import time


# Class to control two kinds of RGB LED Lights / controllers.
# This is just a start, an exploration of the protocol
# 
class LedLight:
    def __init__(self, ipAddr, ipPort, ledType):
        self.ipAddr = ipAddr
        self.ipPort = ipPort
        self.ledType = ledType
        
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
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([49,red, green, blue, 0, 240, 15])))
        else:
            return self.xmit(self.convertToBin([0x56,red, green, blue, 0xAA]))
        
    # Send a white message    
    def sendWhite(self, white):
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([49,0, 0, 0, white, 15, 15])))
        else:
            return self.sendRGB(white, white, white)

    def fadeIn(self):
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([113,35,15])))

    def fadeOut(self):
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([113,36,15])))

    def turnOff(self):
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([113,36,15])))
        else:
            return self.xmit(self.convertToBin([0xCC, 0x24,0x33]))

    def turnOn(self):
        if self.ledType == 1:
            return self.xmit(self.convertToBin(self.addChkSum([113,35,15])))
        else:
            return self.xmit(self.convertToBin([0xCC, 0x23,0x33]))

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
 
