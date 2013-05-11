#!/usr/bin/python
from libthermalraspi.database.SensorDAO import SensorDAO
from libthermalraspi.database.MeasurementDAO import MeasurementDAO
from libthermalraspi.database.Measurement import Measurement
from libthermalraspi.database.DataStoreSQL import DataStoreSQL
import datetime
import unittest
import sqlite3
import os


class DBAccesstest(unittest.TestCase):
    def setUp(self):
        connection = sqlite3.connect(":memory:") #sqlite3.connect(os.path.dirname(__file__)+os.sep+"resources"+os.sep+"test_dbaccess" + os.sep + "sensordb.sqlite")
        self._datastore = DataStoreSQL(connection)
        
        setupfile = open(os.path.dirname(__file__)+os.sep+"resources"+os.sep+"test_dbaccess" + os.sep + "dbaccesstestsetup.sql",'r')
        query = setupfile.read()
        setupfile.close()
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        cursor.close()

    def assertResultByFile(self,result,filename):
        file = open(os.path.dirname(__file__)+os.sep+"resources"+os.sep+"test_dbaccess" + os.sep + filename,'r')
        expectedResult = file.read()
        file.close()
        self.assertEqual(expectedResult,result)

    def test_showSensors(self):
        sensorlist = SensorDAO.readAllSensors(self._datastore.get_Database())
        result = ""
        for s in sensorlist:
            result += s.getName() + "\n"
        self.assertResultByFile(result,"test_showSensors.txt")

    def test_insertSampleMeasure(self):
        sensors = SensorDAO.readAllSensors(self._datastore.get_Database())
        measure = MeasurementDAO(sensors[0].getName(),datetime.datetime.now(),0.0,None)
        measure.insert(self._datastore.get_Database())

    def test_showAllMeasurements(self):
        sensorlist = SensorDAO.readMeasurements(self._datastore.get_Database())
        result = ""
        for s in sensorlist:
            for m in s.getMeasurements():
                result += str(m) + "\n"
        self.assertResultByFile(result,"test_showAllMeasurements.txt")

    def test_ShowMeasurementsOfSensor(self):
        sensor = SensorDAO.readAllSensors(self._datastore.get_Database())[0]
        sensor.readMyMeasurements(self._datastore.get_Database())
        result = ""
        for m in sensor.getMeasurements():
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_ShowMeasurementsOfSensor.txt")

    def test_ShowMeasurementsWithFilter(self):
        sensorlist = SensorDAO.readMeasurements(self._datastore.get_Database(), \
                topCount=1, \
                #sensorIDs=[1,3,4], \
                fromTimestamp=datetime.datetime.strptime("2013-01-01 00:00","%Y-%m-%d %H:%M"), \
                toTimestamp=datetime.datetime.strptime("2013-01-01 23:58","%Y-%m-%d %H:%M"), \
            )
        result = ""
        for s in sensorlist:
            for m in s.getMeasurements():
                result += str(m) + "\n"
        self.assertResultByFile(result,"test_ShowMeasurementsWithFilter.txt")

    def test_addSample(self):
        self._datastore.add_sample(datetime.datetime.strptime("2013-01-30 23:59","%Y-%m-%d %H:%M"),"testsensor",33.33,"Mein Error")
        measurements = self._datastore.get_samples()
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_addSample.txt")

    def test_get_samples(self):
        measurements = self._datastore.get_samples(datetime.datetime.strptime("2013-01-01 00:00","%Y-%m-%d %H:%M"),datetime.datetime.strptime("2013-01-01 23:58","%Y-%m-%d %H:%M"))
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_get_samples.txt")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(DBAccesstest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass

