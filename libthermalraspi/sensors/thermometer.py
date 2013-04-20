import abc

# Abstract base class for Thermometer objects
# get_temperature abstract interface
class Thermometer(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_temperature(self):
        return
    pass
