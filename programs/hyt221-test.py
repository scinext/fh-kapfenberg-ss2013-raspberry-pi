#!/usr/bin/env python

from libthermalraspi.sensors.hyt221 import Hyt221
from libthermalraspi.sensors.hyt221_smbus import Hyt221SMBus


hyt1 = Hyt221(1, 0x28)
print("read/write implementation:")
print("Temperature: %s" % hyt1.get_temperature())
print("Humidity: %s" % hyt1.get_humidity())

hyt2 = Hyt221(1, 0x28)
print("smbus implementation:")
print("Temperature: %s" % hyt2.get_temperature())
print("Humidity: %s" % hyt2.get_humidity())

