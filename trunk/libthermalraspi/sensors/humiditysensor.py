import abc

class HumiditySensor(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_humidity(self):
        return
    
