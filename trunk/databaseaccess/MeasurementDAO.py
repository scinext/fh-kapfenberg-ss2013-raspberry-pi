from databaseaccess.Measurement import Measurement
import databaseaccess
import sqlite3

class MeasurementDAO(Measurement):
    def __init__(self,sensorname,timestamp,measureVal,errorCode):
	    Measurement.__init__(self,sensorname,timestamp,measureVal,errorCode)

    def insert(self,connection):
        MeasurementDAO.insertMeasurement(connection,self)

    @staticmethod
    def insertMeasurement(connection,measurement):
        #Speichert das aktuelle Objekt in die Datenbank
        cursor = connection.cursor()
        insertValues = {
            "sensorid":databaseaccess.SensorDAO.SensorDAO.getSensorId(connection,measurement._sensorname),
            "timestamp": measurement._timestamp,
            "value": measurement._measureVal,
            "errorcode": measurement._errorCode}
        cursor.execute("INSERT INTO measurements " +
            "(sensorid,timestamp,value,errorcode) " +
            " VALUES (:sensorid,:timestamp,:value,:errorcode)",insertValues)
        connection.commit()
