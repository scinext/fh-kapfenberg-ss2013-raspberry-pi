import test_simulation

import unittest

suite = unittest.TestSuite()
suite.addTest(test_simulation.suite)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
