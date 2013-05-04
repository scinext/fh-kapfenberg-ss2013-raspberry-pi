#!/usr/bin/python

from libthermalraspi.sensors.simulation import CyclicThermometer
from libthermalraspi.sensors.thermometer import Thermometer
import os
import sys

_listSensors = []
_listSensors.append(CyclicThermometer([5]))
_listSensors.append(CyclicThermometer([10]))
_listSensors.append(CyclicThermometer([45]))

_listTemperatures = []

_childProcesses = []

_r, _w = os.pipe()

for listSensor in _listSensors:
    print("next sensor") 
    newpid = os.fork()
    if newpid == 0: # parent process
       os.close(_r)
       _w = os.fdopen(_w, 'w')
       print "child: writing - " + str(listSensor.get_temperature())
       _w.write(str(listSensor.get_temperature())+ "\n")
       _w.close()
       print "child: closing"
       os._exit(0)
    else:
       _childProcesses.append(newpid)           

os.close(_w)
_r = os.fdopen(_r) # turn r into a file object
for childProcess in _childProcesses:
   os.waitpid(childProcess, 0)
   temperature = _r.readline()
   print "parent: reading from " + str(childProcess) + " => temperature is " + temperature  
   _listTemperatures.append(temperature)
   
_listTemperatures = map(float, _listTemperatures)
avgTemperature = sum(_listTemperatures) / len(_listTemperatures)

print "****************************************"
print "Durchschnittstemperatur betraegt: " + str(avgTemperature)
print "****************************************"
            