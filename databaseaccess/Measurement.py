class Measurement:
    def __init__(self,sensor,timestamp,measureVal,errorCode):
        #[Sensor]-Objekt
        self._sensor = sensor
        self._timestamp = timestamp
        self._measureVal = measureVal
        self._errorCode = errorCode

    def getSensorname(self):
        return self._sensor.getName()

    def getTimestamp(self):
        return self._timestamp

    def getMeasureVal(self):
        return self._measureVal

    def getErrorCode(self):
        return self._errorCode
