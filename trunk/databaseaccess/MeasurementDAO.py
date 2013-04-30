
from databaseaccess.Measurement import Measurement
from databaseaccess import DBProvider
import sqlite3

class MeasurementDAO(Measurement):
    def __init__(self,sensor,timestamp,measureVal,errorCode):
	    Measurement.__init__(self,sensor,timestamp,measureVal,errorCode)

    def insert(self):
        #Speichert das aktuelle Objekt in die Datenbank
        connection = DBProvider.getDBConncetion()
        cursor = connection.cursor()
        insertValues = {
            "sensorid":self._sensor.getId(),
            "timestamp": self._timestamp,
            "value": self._measureVal,
            "errorcode": self._errorCode}
        cursor.execute("INSERT INTO measurements " +
            "(sensorid,timestamp,value,errorcode) " +
            " VALUES (:sensorid,:timestamp,:value,:errorcode)",insertValues)
        connection.commit()
