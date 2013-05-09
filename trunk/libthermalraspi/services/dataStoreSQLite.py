#!/usr/bin/python
from libthermalraspi.services.dataStore import DataStore
from databaseaccess.SensorDAO import SensorDAO
from databaseaccess.MeasurementDAO import MeasurementDAO

class DataStoreSQLite(DataStore):
    """Verbindungsklasse zur Abstraktion des Datenbankzugriffs."""

    def __init__(self):
        pass

    def get_sample(self, fromDatetime, toDatetime, maxResultCount = None, sensorIDs = None):
        """Anzahl von Messwerten eines Zeitraumes aus der Datenbank auslesen.
           Parameter:
           fromDatetime   -- Timestamp, Anfangszeitpunkt der Messwerte
           toDatetime     -- Timestamp, Endzeitpunkt der Messwerte
           maxResultCount -- int, maximale Anzahl der auszulesenden Messwerte - Standardwert: None
           sensorIDs      -- int[], Liste der auszulesenden SensorenIDs wie in der Datenbank gespeichert - Standardwert: None
        """
        return SensorDAO.readMeasurements(fromDatetime, toDatetime, maxResultCount, sensorIDs)
        pass
     
    def add_sample(self, timestamp, sensorname, temperatur, status):
        """Messwert eines bestimmten Sensors in die Datenbank schreiben.
           Parameter:
           timestamp    -- Timestamp, Zeitstempel der Uhrzeit des Messwertes
           sensorname   -- String, Bezeichnung des messenden Sensors 
           temperatur   -- float, Wert der gemessenen Temperatur
           status       -- int, Status des Sensors
        """
        sample = MeasurementDAO(sensorname, timestamp, temperatur, status)
        sample.insert()
        pass
    
