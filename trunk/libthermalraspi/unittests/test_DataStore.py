#!/usr/bin/python
from libthermalraspi.database.Measurement import Measurement
from libthermalraspi.database.DataStoreInMemory import DataStoreInMemory
from libthermalraspi.database.DataStoreSQL import DataStoreSQL
import datetime
import unittest
import sqlite3
import os


class Datastoretest(unittest.TestCase):
    def setUp_InMemory(self):
        self._datastore = DataStoreInMemory()

    def setUp_SQL(self):
        connection = sqlite3.connect(":memory:")
        self._datastore = DataStoreSQL(connection)

        setupfile = open(os.path.dirname(__file__)+os.sep+"resources"+os.sep+"test_DataStore" + os.sep + "dbaccesstestsetup.sql",'r')
        query = setupfile.read()
        setupfile.close()
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        cursor.close()

    def assertResultByFile(self,result,filename):
        file = open(os.path.dirname(__file__)+os.sep+"resources"+os.sep+"test_DataStore" + os.sep + filename,'r')
        expectedResult = file.read()
        file.close()
        self.assertEqual(expectedResult,result)

    def test_add_sample_SQL(self):
        self.setUp_SQL()
        self.initDataForSqlStore()
        measurements = self._datastore.get_samples()
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_addSample.txt")

    def test_add_sample_InMemory(self):
        self.setUp_InMemory()
        self._datastore.initSomeTestData()
        measurements = self._datastore.get_samples()
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_addSample.txt")

    def test_get_samples_SQL(self):
        self.setUp_SQL()
        self.initDataForSqlStore()
        measurements = self._datastore.get_samples(datetime.datetime.strptime("2013-01-30 23:57","%Y-%m-%d %H:%M"),datetime.datetime.strptime("2013-01-30 23:58","%Y-%m-%d %H:%M"))
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_get_samples.txt")

    def test_get_samples_InMemory(self):
        self.setUp_InMemory()
        self._datastore.initSomeTestData()
        measurements = self._datastore.get_samples(datetime.datetime.strptime("2013-01-30 23:57","%Y-%m-%d %H:%M"),datetime.datetime.strptime("2013-01-30 23:58","%Y-%m-%d %H:%M"))
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_get_samples.txt")

    def initDataForSqlStore(self):
        self._datastore.add_sample(datetime.datetime.strptime("2013-01-30 23:57:38","%Y-%m-%d %H:%M:%S"),"Strawberry",20.12,0)
        self._datastore.add_sample(datetime.datetime.strptime("2013-01-30 23:57:37","%Y-%m-%d %H:%M:%S"),"Raspberry",30.0,0)
        self._datastore.add_sample(datetime.datetime.strptime("2013-01-30 23:58:36","%Y-%m-%d %H:%M:%S"),"Banana",27.132,1)
        self._datastore.add_sample(datetime.datetime.strptime("2013-01-30 23:59:35","%Y-%m-%d %H:%M:%S"),"Blackberry",27.132,0)



suite = unittest.defaultTestLoader.loadTestsFromTestCase(Datastoretest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass

