from __future__ import with_statement
from libthermalraspi.sensors.lm73device import LM73Device
from libthermalraspi.sensors.lm73device import ResolutionEnum

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

    def test_getResolution(self):
        #48: 0011 0000
        #32: 0010 0000
        #16: 0001 0000
        #00: 0000 0000

        #240: 1111 0000

        testDict= {240:3, 48:3, 32:2, 16:1,0:0, 255:3}
        for key,val in testDict.iteritems():
            #print("key:" + str(key)+" value:"+ str(testDict[key]))
            binaryData = struct.pack("B", key)
            result = LM73Device.resolveResolution(binaryData)
            self.assertEqual(testDict[key], result)

        pass

    def test_setResolution(self):
        binary_255 = bin(255)
        self.assertEqual(bin(207), LM73Device.getManipulatedResolution(binary_255,ResolutionEnum.ZERO))
        self.assertEqual(bin(223), LM73Device.getManipulatedResolution(binary_255,ResolutionEnum.ONE))
        self.assertEqual(bin(239), LM73Device.getManipulatedResolution(binary_255,ResolutionEnum.TWO))
        self.assertEqual(binary_255, LM73Device.getManipulatedResolution(binary_255,ResolutionEnum.THREE))

        binary_1=bin(1)
        self.assertEqual(binary_1, LM73Device.getManipulatedResolution(binary_1,ResolutionEnum.ZERO))
        self.assertEqual(bin(17), LM73Device.getManipulatedResolution(binary_1,ResolutionEnum.ONE))
        self.assertEqual(bin(33), LM73Device.getManipulatedResolution(binary_1,ResolutionEnum.TWO))
        self.assertEqual(bin(49), LM73Device.getManipulatedResolution(binary_1,ResolutionEnum.THREE))
        pass

    def test_setInvalidResolution(self):
        with self.assertRaises(Exception):
            LM73Device.getManipulatedResolution(bin(1),4)
    pass

suite = unittest.defaultTestLoader.loadTestsFromTestCase(LM73DeviceTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass