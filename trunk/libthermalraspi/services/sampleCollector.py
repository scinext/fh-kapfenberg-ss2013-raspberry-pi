import abc

"""Abstract base class for SampleCollector for gathering
sensor measurment data"""
class SampleCollector(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self, store, sensorList = {}):
        """Collector mit Datenspeicher und Dictionary der abzufragender
        Sensoren übergeben.
        
        @param store: Datenbank-Connection
        @param sensorList: Dictionary SensorName : SensorInstanz
        """
        return        
    
    @abc.abstractmethod
    def run(self, looper):
        """Messungen starten und per externem iterierbarem Objekt
        (looper) Intervall der Messzyklen festlegen.
        
        @param looper: Iterierbares Objekt/List/...
        """
        return        

