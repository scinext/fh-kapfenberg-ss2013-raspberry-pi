#!/usr/bin/env python

from libthermalraspi.sensors.ad7414 import AD7414Thermometer

# Create the I2CDevice with bus no. and device address
ad7414 = AD7414Thermometer(1, 0x49)

print "AD7414 I2C-implementation:"
print("Temperature: %s" % ad7414.get_temperature())

