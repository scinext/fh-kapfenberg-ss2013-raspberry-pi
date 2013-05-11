class Measurement:
    def __init__(self,sensorname,timestamp,measureVal,errorCode):
        assert type(sensorname) is str
		
        #[Sensor]-Objekt
        self._sensorname = sensorname
        self._timestamp = timestamp
        self._measureVal = measureVal
        self._errorCode = errorCode

    def getSensorname(self):
        return self._sensorname

    def getTimestamp(self):
        return self._timestamp

    def getMeasureVal(self):
        return self._measureVal

    def getErrorCode(self):
        return self._errorCode

    def __str__(self):
        return self._sensorname + ";" + str(self._timestamp) + ";" + str(self._measureVal) + ";" + str(self._errorCode)