from libthermalraspi.database.MeasurementDAO import MeasurementDAO
from libthermalraspi.database.SensorDAO import SensorDAO
from libthermalraspi.database.DataStore import DataStore

class DataStoreSQL(DataStore):
    def __init__(self,db):
        self._db = db

    def get_samples(self,fromTimestamp=None,toTimestamp=None):
        """Anzahl von Messwerten eines Zeitraumes aus der Datenbank auslesen.
           Parameter:
           fromDatetime   -- Timestamp, Anfangszeitpunkt der Messwerte
           toDatetime     -- Timestamp, Endzeitpunkt der Messwerte
        """
        sensors = SensorDAO.readMeasurements(self._db,fromTimestamp=fromTimestamp,toTimestamp=toTimestamp)
        measurements = []
        for s in sensors:
            for m in s.getMeasurements():
                measurements.append(m)
        return measurements

    def add_sample(self, timestamp, sensorname, temperatur, status):
        """Messwert eines bestimmten Sensors in die Datenbank schreiben.
           Parameter:
           timestamp    -- Timestamp, Zeitstempel der Uhrzeit des Messwertes
           sensorname   -- String, Bezeichnung des messenden Sensors 
           temperatur   -- float, Wert der gemessenen Temperatur
           status       -- int, Status des Sensors
        """
        sample = MeasurementDAO(sensorname, timestamp, temperatur, status)
        sample.insert(self._db)
        pass

    def get_Database(self):
        return self._db