import test_simulation
import test_lm73device

import unittest

suite = unittest.TestSuite()
suite.addTest(test_simulation.suite)
suite.addTest(test_lm73device.suite)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
