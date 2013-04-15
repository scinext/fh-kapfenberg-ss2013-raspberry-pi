from libthermalraspi.sensors.simulation import CyclicThermometer

import unittest

class SimulationTest(unittest.TestCase):
    def test__cylic(self):
        th = CyclicThermometer([1, 2.5, 3])

        self.failUnlessAlmostEqual(th.get_temperature(), 1)
        self.failUnlessAlmostEqual(th.get_temperature(), 2.5)
        self.failUnlessAlmostEqual(th.get_temperature(), 3)
        self.failUnlessAlmostEqual(th.get_temperature(), 1)
        pass
    pass

suite = unittest.defaultTestLoader.loadTestsFromTestCase(SimulationTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
