class Sensor:
    def __init__(self,id,name):
        self._id = id
        self._name = name
        #Liste von [Measurement]
        self._measures = []

    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getMeasurements(self):
        return self._measures

    def addMeasurement(self,measure):
        self._measures.append(measure)

    def __str__(self):
        return self._name;

    @staticmethod
    def hasId(sensor,id):
        if sensor is None:
            return False
        elif sensor.getId() == id:
            return True
        else:
            return False
