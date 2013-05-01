import unittest
from libthermalraspi.sensors.compositeThermometer_SWD11G2_3 import CompositeThermometer
from libthermalraspi.sensors.simulation import CyclicThermometer

class CompositeSensor_SWD11G2_3Test(unittest.TestCase):
    def test__CyclicThermometers(self):
        sensors = []
        sensors.append(CyclicThermometer([10]))
        sensors.append(CyclicThermometer([10]))
        
        ct = CompositeThermometer()
        ct.add_sensors(sensors)
        self.failUnlessAlmostEqual(ct.get_temperature(), 10.0) 


    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(CompositeSensor_SWD11G2_3Test)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
