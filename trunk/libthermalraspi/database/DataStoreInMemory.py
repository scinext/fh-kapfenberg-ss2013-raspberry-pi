import datetime
from libthermalraspi.database.DataStore import DataStore
from libthermalraspi.database.Measurement import Measurement

class DataStoreInMemory(DataStore):
    def __init__(self):
        self._measures = []

    def get_samples(self,fromTimestamp=None,toTimestamp=None):
        return sorted( \
					sorted( \
						(filter(lambda m: (toTimestamp==None or m.getTimestamp() <= toTimestamp) and (fromTimestamp==None or m.getTimestamp() >= fromTimestamp),self._measures)) \
					,key=lambda m: m.getTimestamp(),reverse=True) \
				,key=lambda m: m.getSensorname())

    def add_sample(self,timestamp, sensorname, temperatur, status):
        self._measures.append(Measurement(sensorname, timestamp, temperatur, status))

    def initSomeTestData(self):
        self.add_sample(datetime.datetime.strptime("2013-01-30 23:57:38","%Y-%m-%d %H:%M:%S"),"Strawberry",20.12,0)
        self.add_sample(datetime.datetime.strptime("2013-01-30 23:57:37","%Y-%m-%d %H:%M:%S"),"Raspberry",30.0,0)
        self.add_sample(datetime.datetime.strptime("2013-01-30 23:58:36","%Y-%m-%d %H:%M:%S"),"Banana",27.132,1)
        self.add_sample(datetime.datetime.strptime("2013-01-30 23:59:35","%Y-%m-%d %H:%M:%S"),"Blackberry",27.132,0)