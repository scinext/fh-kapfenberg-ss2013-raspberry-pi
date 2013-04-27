import datetime

class SensorDAO(Sensor):
   	def __init__(self,id,name):
		self._init__(self,id,name)
		
	def readMeasurements(self,fromTimestamp=None,toTimestamp=datetime.datetime.now(),topCount=None):
		#Liest alle Messungen entsprechend dem Filter zum aktuellen Sensor  aus der Datenbank und speichert sie im Objekt
		self._measures = readMeasurements(fromTimestamp,toTimestamp,topCount,[self._id])[0].getMeasurements()
		return self._measures
		
	def readMeasurements(fromTimestamp=None,toTimestamp=datetime.datetime.now(),topCount=None,sensorIDs=None):
		#Liest alle Messungen entsprechend dem Filter aus der Datenbank und gibt sie als Sensorliste zurück
		#fromTimestamp datetime: Von einem Eintragszeitpunkt
		#toTimestamp datetime: Bis zu einem Eintragszeitpunkt
		#topCount int: Maximale Anzahl an zurückggebenen Messwerten pro Sensor
		#sensorIDs [int]: Filterung nach den übergebenen Sensord-ID
		sensors = []
		return sensors;
		
	def readAllSensors():
		#Liest alle in der Datenbank gespeicherten Sensoren aus
		#Messwerte sind nicht enthalten
		#Liste von [Sensor]
		sensors = []
		return sensors