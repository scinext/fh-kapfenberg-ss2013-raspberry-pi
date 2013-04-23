#!/usr/bin/python

from libthermalraspi.sensors.tc74 import TC74Thermometer

t= TC74Thermometer (1, 0x4d)
print("Temperature: %s" %t.get_temperature())