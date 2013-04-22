from libthermalraspi.sensors.lm73device import LM73Device

import unittest
import struct

class LM73DeviceTest(unittest.TestCase):
    def test__temp_creation(self):        
        tmp = struct.pack("BB", 12, 176)
        msb, lsb = struct.unpack("BB", tmp)        
        self.assertAlmostEqual(25.375, LM73Device.create_temperature(msb, lsb), 7, "", 0.000001)
        
        tmp = struct.pack("BB", 140, 176)
        msb, lsb = struct.unpack("BB", tmp)
                            
        self.assertAlmostEqual(-25.375, LM73Device.create_temperature(msb, lsb), 7, "", 0.000001)

        pass
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(LM73DeviceTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass