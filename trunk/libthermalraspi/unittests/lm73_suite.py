import hwtest_lm73device

import unittest

suite = unittest.TestSuite()
suite.addTest(hwtest_lm73device.suite)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
