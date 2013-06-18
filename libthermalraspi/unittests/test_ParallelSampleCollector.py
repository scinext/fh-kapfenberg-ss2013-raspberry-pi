# Team: Martin Krainer, Markus Koller

from libthermalraspi.sensors.simulation_sensorstub import SensorStub
from libthermalraspi.sensors.storemock import StoreMock
from libthermalraspi.sensors.services.parallelSampleCollector import ParallelSampleCollector

import unittest

class ParallelSampleCollectorTest(unittest.TestCase):
    def test__parallel(self):
        # Setup
		# Liste mit Testmessungen
		measurements = [ 1, 2, 5, -9, -6 ]
 
		# Sensor-Stub anlegen
		sensor = SensorStub(measurements)
 
		# Store-Mock anlegen
		store = StoreMock()
 
		# Dictionary aus Sensoren erzeugen (In diesem Fall nur ein Eintrag...)
		sensorList = { "test-sensor1" : sensor }
 
		# Exercise-Phase:
		collector = ParallelSampleCollector(store, sensors)
		collector.run(measurements)
 
		# Verify TODO:
		# Jetzt müssen alle Werte von measurements in store sein...
		# Wenn ja -> Test OK	

suite = unittest.defaultTestLoader.loadTestsFromTestCase(ParallelSampleCollectorTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass