from databaseaccess.MeasurementDAO import MeasurementDAO
from databaseaccess.SensorDAO import SensorDAO
from databaseaccess.DataStore import DataStore

class DataStoreSQL(DataStore):
    def __init__(self,db):
        self._db = db
		
    def get_samples(self,fromTimestamp=None,toTimestamp=None):
        sensors = SensorDAO.readMeasurements(self._db,fromTimestamp=fromTimestamp,toTimestamp=toTimestamp)
        measurements = []
        for s in sensors:
            for m in s.getMeasurements():
                measurements.append(m)
        return measurements

    def add_sample(self,measurement):
        MeasurementDAO.insertMeasurement(self._db,measurement)
	
    def get_Database(self):
        return self._db