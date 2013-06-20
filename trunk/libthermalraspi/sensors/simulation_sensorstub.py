#SensorStub simuliert die Temperaturmessungen und erhaelt einfach eine Liste 
#mit Messwerten, die als Testeingangswerte dienen.

from libthermalraspi.sensors.thermometer import Thermometer

# SensorStub erhaelt eine Liste an Messwerten, die
# in get_temperature zurueck geliefert werden.
# Dieser Test-Stub wird verwendet um im ParallelSampleCollector
# Messungen zu simulieren.
class SensorStub(Thermometer):
    def __init__(self, measurements = []):
        self.__measurements = measurements;
        self.__index = 0
    
    def get_temperature(self):
        self.__index = self.__index + 1
        
        if self.__index >= self.__measurements.length:
            self.__index = 0
            
        return self.__measurements[self.__index]
		
