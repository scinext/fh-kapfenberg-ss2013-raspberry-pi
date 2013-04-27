class Measurement:
   	def __init__(self,sensor,timestamp,measureVal,errorCode):
		#[Sensor]-Objekt
		self._sensor = sensor
		self._timestamp = timestamp
		self._measureVal = measureVal
		self._errorCode = errorCode
		
	def getSensorname():
		return self._sensor.getName()

	def getTimestamp():
		return self._timestamp
		
	def getMeasureVal():
		return self._measureVal
		
	def getErrorCode():
		return self._errorCode