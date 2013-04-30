#!/usr/bin/python
from databaseaccess.SensorDAO import SensorDAO
from databaseaccess.MeasurementDAO import MeasurementDAO
import datetime
import unittest

class DBAccesstest(unittest.TestCase):
    def test_showSensors(self):
        sensorlist = SensorDAO.readAllSensors()
        print("Sensors available(" + str(len(sensorlist)) + "):")
        for s in sensorlist:
            print(" - " +s.getName())

    def test_insertSampleMeasure(self):
        sensors = SensorDAO.readAllSensors()
        measure = MeasurementDAO(sensors[0],datetime.datetime.now(),0.0,None)
        measure.insert()

    def test_showAllMeasurements(self):
        sensorlist = SensorDAO.readMeasurements()
        print("Measurements available:")
        for s in sensorlist:
            for m in s.getMeasurements():
                print(" - " + str(m))

    def test_ShowMeasurementsOfSensor(self):
        sensor = SensorDAO.readAllSensors()[0]
        sensor.readMyMeasurements()
        print("Measurements of " + str(sensor) + ":")
        for m in sensor.getMeasurements():
                print(" - " + str(m))

    def test_ShowMeasurementsWithFilter(self):
        sensorlist = SensorDAO.readMeasurements( \
                topCount=2, \
                sensorIDs=[1,3,4], \
                fromTimestamp=datetime.datetime.strptime("2013-04-27 21:15","%Y-%m-%d %H:%M"), \
                toTimestamp=datetime.datetime.strptime("2013-04-28 13:31","%Y-%m-%d %H:%M"), \
            )
        print("Measurements available for filter:")
        for s in sensorlist:
            for m in s.getMeasurements():
                print(" - " + str(m))

suite = unittest.defaultTestLoader.loadTestsFromTestCase(DBAccesstest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass

#if __name__ == '__main__':
#    showSensors()
#    showAllMeasurements()
#    ShowMeasurementsOfSensor()
#    ShowMeasurementsWithFilter()
#    #insertSampleMeasure()
#    print("all tests finished")

