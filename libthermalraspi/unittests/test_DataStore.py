#!/usr/bin/python
from databaseaccess.Measurement import Measurement
from databaseaccess.InMemoryDataStore import InMemoryDataStore
from databaseaccess.DataStoreSQL import DataStoreSQL
import datetime
import unittest
import sqlite3
import os


class DBAccesstest(unittest.TestCase):
    def setUp_InMemory(self):
        self._datastore = InMemoryDataStore()
		
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
        self.add_sample()

    def test_add_sample_InMemory(self):
        self.setUp_InMemory()
        self.add_sample()

    def test_get_samples_SQL(self):
        self.setUp_SQL()
        self.get_samples()

    def test_get_samples_InMemory(self):
        self.setUp_InMemory()
        self.get_samples()
	
    def add_sample(self):
        self._datastore.add_sample(Measurement("testsensor",datetime.datetime.strptime("2013-01-30 23:56","%Y-%m-%d %H:%M"),33.33,"Mein Error"))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:57","%Y-%m-%d %H:%M"),0.0,None))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:58","%Y-%m-%d %H:%M"),1.33,None))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:59","%Y-%m-%d %H:%M"),1.35,None))
        measurements = self._datastore.get_samples()
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_addSample.txt")
		
    def get_samples(self):
        self._datastore.add_sample(Measurement("testsensor",datetime.datetime.strptime("2013-01-30 23:56","%Y-%m-%d %H:%M"),33.33,"Mein Error"))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:57","%Y-%m-%d %H:%M"),0.0,None))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:58","%Y-%m-%d %H:%M"),1.33,None))
        self._datastore.add_sample(Measurement("testsensor2",datetime.datetime.strptime("2013-01-30 23:59","%Y-%m-%d %H:%M"),1.35,None))
        measurements = self._datastore.get_samples(datetime.datetime.strptime("2013-01-30 23:57","%Y-%m-%d %H:%M"),datetime.datetime.strptime("2013-01-30 23:58","%Y-%m-%d %H:%M"))
        result = ""
        for m in measurements:
            result += str(m) + "\n"
        self.assertResultByFile(result,"test_get_samples.txt")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(DBAccesstest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass

