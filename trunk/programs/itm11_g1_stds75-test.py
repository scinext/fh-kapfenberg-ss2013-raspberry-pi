#!/usr/bin/env python

from libthermalraspi.sensors.itm11_g1_stds75 import Stds75
import time


stds75 = Stds75(0, 0x4e)
print "read/write implementation:"

while(True):
    print("Temperature: %f" % stds75.get_temperature())
    time.sleep(1)
