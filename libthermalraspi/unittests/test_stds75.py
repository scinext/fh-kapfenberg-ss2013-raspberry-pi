#!usr/bin/python

from libthermalraspi.sensors.stds75 import Stds75

t = Stds75(1, 0x4e)
t.get_temperature()

