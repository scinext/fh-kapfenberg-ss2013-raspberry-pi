class DataStoreStdOut(object):
    def get_sample(self, fromDatetime, toDatetime, maxResultCount = None, sensorIDs = None):
        assert False, 'cannot get samples from stdout'
     
    def add_sample(self, timestamp, sensorname, temperatur, status):
        print timestamp, sensorname, temperatur, status
    
