#!/usr/bin/python

from phue import Bridge

b = Bridge('192.168.1.50')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
print b.get_api()

print b.get_light_objects()
