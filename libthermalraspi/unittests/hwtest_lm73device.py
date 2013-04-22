'''
Created on 22.04.2013

@author: Helmut
'''

from libthermalraspi.sensors.lm73device import LM73Device

import unittest

class LM73DeviceHWTest(unittest.TestCase):
    def test__resolution(self):
        dev = LM73Device(1, 47)
        res = dev.get_resolution()
        # todo...
        dev.set_resolution(res)
        # verify...
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(LM73DeviceHWTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
