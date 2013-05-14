import unittest
from libthermalraspi.sensors.composite_g2_3 import CompositeSensor
from libthermalraspi.sensors.simulation import CyclicThermometer

class CompositeSensor_G2_3Test(unittest.TestCase):
    def test__CyclicThermometers(self):
        sensors = []
        sensors.append(CyclicThermometer([10]))
        sensors.append(CyclicThermometer([10]))
        
        ct = CompositeSensor()
        ct.add_sensors(sensors)
        self.failUnlessAlmostEqual(ct.get_temperature(), 10.0) 
        pass
    pass

    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(CompositeSensor_G2_3Test)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
