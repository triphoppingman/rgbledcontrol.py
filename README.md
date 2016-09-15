# rgbledcontrol.py
Control a variety of RGB LED WiFi bulbs and controllers

This code is my first attempt at python coding so it will, no doubt, 
contain many unpleasant coding errors, especially in terms of style.

##What is this library for
Provides an interface to some of the low cost RGB LED WIFI bulbs and
LED strip controllers based on the ESP8266 low cost WIFI interface
module.   It provides an abstraction of the various functions of both 
kinds (bulbs and WIFI370 modules).   It also incorporates a twisted
internet server so that high level commands may be interpreted (via
PyParsing) and executed.   Grouping structures are supported.

## Warrantees etc.
I don't warrantee a thing - in fact expect everything to break.

## Getting started.
Take a look at the test.py example in the src directory.   This will give
a good idea of the capabilities


