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

suite = unittest.defaultTestLoader.loadTestsFromTestCase(LM73DeviceTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass