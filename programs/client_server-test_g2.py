#!/usr/bin/python

from libthermalraspi.sensors.thermo_proxy_itmG2 import ThermoProxy_ItmG2

t= ThermoProxy_ItmG2()
print("Temperature: %s" %t.get_temperature())
