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