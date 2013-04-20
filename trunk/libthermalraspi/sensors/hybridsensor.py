import abc

from libthermalraspi.sensors.thermometer import Thermometer

# Abstract base class for hybrid sensor
# get_humidity abstract interface
class HybridSensor(Thermometer):
    __metaclass__ = abc.ABCMeta
        
    @abc.abstractmethod
    def get_humidity(self):        
        return
    
