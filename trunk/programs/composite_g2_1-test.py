#!/usr/bin/env python

from libthermalraspi.sensors.composite_g2_1 import CompositeSensor
from libthermalraspi.sensors.simulation import CyclicThermometer

t = CompositeSensor()
t.append_sensor(CyclicThermometer([5]))
t.append_sensor(CyclicThermometer([10]))
t.append_sensor(CyclicThermometer([45]))

print("AVG temperature: %s" % t.get_temperature())