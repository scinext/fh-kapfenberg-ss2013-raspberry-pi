# StoreMock sammelt die Messungen, die der ParallelSampleCollector 
# auf SensorStub durchführt.

class StoreMock(object):
    def __init__(self):
        self.__samples = []
        
    def add_sample(self, timestamp, sensorname, temperatur, status):
        self.__samples.append((timestamp, sensorname, temperatur, status))
        
    def __iter__(self):
        for (timestamp, sensorname, temperatur, status) in self.__samples:
            yield (timestamp, sensorname, temperatur, status)
