import datetime
from databaseaccess.DataStore import DataStore

class InMemoryDataStore(DataStore):
    def __init__(self):
        self._measures = []

    def get_samples(self,fromTimestamp=None,toTimestamp=None):
        return sorted( \
					sorted( \
						(filter(lambda m: (toTimestamp==None or m.getTimestamp() <= toTimestamp) and (fromTimestamp==None or m.getTimestamp() >= fromTimestamp),self._measures)) \
					,key=lambda m: m.getTimestamp(),reverse=True) \
				,key=lambda m: m.getSensorname())

    def add_sample(self,measurement):
        self._measures.append(measurement)