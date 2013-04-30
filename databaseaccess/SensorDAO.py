import datetime
from databaseaccess.Sensor import Sensor
from databaseaccess.MeasurementDAO import MeasurementDAO
from databaseaccess import DBProvider
import sqlite3 

class SensorDAO(Sensor):
    def __init__(self,id,name):
        Sensor.__init__(self,id,name)

    def readMyMeasurements(self,fromTimestamp=None,toTimestamp=datetime.datetime.now(),topCount=None):
        #Liest alle Messungen entsprechend dem Filter zum aktuellen Sensor  aus der Datenbank und speichert sie im Objekt
        sensors = SensorDAO.readMeasurements(fromTimestamp,toTimestamp,topCount,[self._id])
        if len(sensors) > 0:
            self._measures = sensors[0].getMeasurements()
        else:
            self._measures = []
        return self._measures

    @staticmethod
    def readMeasurements(fromTimestamp=None,toTimestamp=datetime.datetime.now(),topCount=None,sensorIDs=None):
        #Liest alle Messungen entsprechend dem Filter aus der Datenbank und gibt sie als Sensorliste zurueck
        #fromTimestamp datetime: Von einem Eintragszeitpunkt
        #toTimestamp datetime: Bis zu einem Eintragszeitpunkt
        #topCount int: Maximale Anzahl an zurueckggebenen Messwerten pro Sensor
        #sensorIDs [int]: Filterung nach den uebergebenen Sensord-ID
        if not sensorIDs is None:
            if len(sensorIDs) == 0:
                return []

        #WHERE Query-----------------------------------
        filterValues = {}
        filterQuery = []
        whereExpression = ""
        if not fromTimestamp is None:
            filterValues["fromTimestamp"] = fromTimestamp
            filterQuery.append("m.timestamp >= :fromTimestamp")

        if not toTimestamp is None:
            filterValues["toTimestamp"] = toTimestamp
            filterQuery.append("m.timestamp <= :toTimestamp")

            
        if not topCount is None:
            filterValues["topCount"] = topCount
            tmpFilterForSubquery = ""
            if len(filterQuery) > 0:
                tmpFilterForSubquery = "AND " + " AND ".join([f.replace("m.","") for f in filterQuery])
            filterQuery.append("m.timestamp IN ( " + \
                               "SELECT timestamp FROM measurements " + \
                                   "WHERE sensorid = m.sensorid " + tmpFilterForSubquery +\
                                   " ORDER BY timestamp DESC LIMIT :topCount)")
        if not sensorIDs is None:
            filterQuery.append("s.id IN (" + ",".join([str(id) for id in sensorIDs]) + ")")

        if len(filterQuery) > 0:
            whereExpression = "WHERE " + " AND ".join(filterQuery)
        #---------------------------------------------
        
        cursor = DBProvider.getDBConncetion().cursor()
        sql = "SELECT s.id as sensorid, s.name, m.timestamp, m.value, m.errorcode " + \
                       "FROM sensors s " + \
                       "LEFT JOIN measurements m ON s.id = m.sensorid " + whereExpression + \
                       " ORDER BY s.name, s.id, m.timestamp DESC"
        #print(sql)
        #print(filterValues)
        cursor.execute(sql,filterValues)
        sensors = []
        cSensor = None
        for row in cursor:
            #Abrufe aller Messungen und zuweisung zu den Sensoren
            #Betrifft die aktuelle Zeile einen anderen Sensor wir dieser angelegt.
            if not Sensor.hasId(cSensor,row[0]):
                cSensor = Sensor(row[0],row[1])
                sensors.append(cSensor)

            if not row[2] is None:
                cSensor.addMeasurement(MeasurementDAO(cSensor,row[2],row[3],row[4]))

        return sensors;

    @staticmethod
    def readAllSensors():
        #Liest alle in der Datenbank gespeicherten Sensoren aus
        #Messwerte sind nicht enthalten
        #Liste von [Sensor]
        cursor = DBProvider.getDBConncetion().cursor()
        cursor.execute("SELECT id, name FROM sensors ORDER BY name")
        sensors = []
        for row in cursor:
            sensors.append(SensorDAO(row[0],row[1]))
        return sensors
