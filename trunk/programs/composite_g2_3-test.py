#!/usr/bin/python

from libthermalraspi.unittests import test_compositeThermometer_SWD11G2_3

import unittest

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_compositeThermometer_SWD11G2_3.suite)
    pass
