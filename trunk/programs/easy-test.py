#!/usr/bin/python

from libthermalraspi.unittests import easy_suite

import unittest

if __name__ == '__main__':
    unittest.TextTestRunner().run(easy_suite.suite)
    pass
