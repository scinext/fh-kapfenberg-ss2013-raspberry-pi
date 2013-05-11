import abc

class DataStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sample(self, fromDatetime, toDatetime):
        """Anzahl von Messwerten eines Zeitraumes aus der Datenbank auslesen.
           Parameter:
           fromDatetime   -- Timestamp, Anfangszeitpunkt der Messwerte
           toDatetime     -- Timestamp, Endzeitpunkt der Messwerte
        """
        return
     
    @abc.abstractmethod
    def add_sample(self, timestamp, sensorname, temperatur, status):
        """Messwert eines bestimmten Sensors in die Datenbank schreiben.
           Parameter:
           timestamp    -- Timestamp, Zeitstempel der Uhrzeit des Messwertes
           sensorname   -- String, Bezeichnung des messenden Sensors 
           temperatur   -- float, Wert der gemessenen Temperatur
           status       -- int, Status des Sensors
        """
        return
    
