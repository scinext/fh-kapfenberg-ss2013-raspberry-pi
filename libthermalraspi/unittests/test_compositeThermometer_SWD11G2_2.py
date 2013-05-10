
import unittest
from libthermalraspi.sensors.simulation import CyclicThermometer
from libthermalraspi.sensors.composite_g2_2 import CompositeSensor

class TestCompositeSensor(unittest.TestCase):
         
    def setUp(self):
        self._testSensors = []
        self._composite = CompositeSensor()
        
    def test_getTemperature(self):
        self._testSensors.append( CyclicThermometer([10]) )
        self._testSensors.append( CyclicThermometer([8]) )
        
        self._composite.add_sensors(self._testSensors)
        self.failUnlessAlmostEqual(self._composite.get_temperature(), 9) 
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCompositeSensor)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass