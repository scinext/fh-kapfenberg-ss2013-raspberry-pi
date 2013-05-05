import abc

"""Abstract base class for SampleCollector for gathering
sensor measurment data"""
class SampleCollector(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_temperature(self):
        return
    pass
    
    @abc.abstractmethod
    def configuration(self, sensorNamesList=[] ):
        """Sammler der Messdaten mit Liste aller abzufragenden Sensoren versorgen."""
        return
    
    @abc.abstractmethod
    def run(self, timeDelta):
        """Messungen starten und Zeitintervall zwischen zwei Abfragen
        der Sensormesswerte in Millisekunden festlegen. Messungen erfolgen, bis stop()
        aufgerufen wird."""
        return
    
    @abc.abstractmethod
    def stop(self):
        """Abbruchbedingung aller weiterer Messungen setzen."""
        return
        

