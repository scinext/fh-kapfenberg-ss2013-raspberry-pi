class Sensor:
   	def __init__(self,id,name):
		self._id = id
		self._name = name
		#Liste von [Measurement]
		self._measures = []
		
	def getName(self):
		return self._name
		
	def getMeasurements(self):
		return self._measures
		
	def addMeasurement(self,measure):
		self._measures.add(m)

	def __str__(self):
		return self._name;