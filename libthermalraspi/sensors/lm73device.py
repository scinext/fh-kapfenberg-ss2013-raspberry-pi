# -*- coding: utf-8 -*-

import struct

from libthermalraspi.i2c_device import I2CDevice
from libthermalraspi.sensors.thermometer import Thermometer

# Not yet tested on raspberry
# create_temperature() successfully tested against
# datasheet specs.
class LM73Device(Thermometer, I2CDevice):
    """
    Author: HeKo
    """

    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    def get_temperature(self):
        # select Temperature register
        self.write('\x00')

        # read 2-byte temperature
        data = self.read(2)

        # Temperature register:
        # D15        D14        D13        D12        D11        D10        D9         D8
        # SIGN       128C       64C        32C        16C        8C         4C         2C
        # D7         D6         D5         D4         D3         D2         D1         D0
        # 1C         0.5C       0.25C      0.125C     0.0625C    0.03125C  reserved   reserved

        msb, lsb = struct.unpack('BB', data)

        return LM73Device.create_temperature(msb, lsb)

    def set_resolution(self, resolution):
        #maybe validate input first before reading,
        #but atm i have to validate the input in the static method for easy-testing

        # select Control/Status register
        self.write('\x04')
        # read 1-byte
        binaryData = self.read(1)
        unpackedData =struct.unpack('B', binaryData)

        newBinaryData = LM73Device.getManipulatedResolution(unpackedData[0], resolution)
        self.write(struct.pack('B', newBinaryData))

    def get_resolution(self):
        # select Control/Status register
        self.write('\x04')
        # read 1-byte
        binaryData = self.read(1)
        # Control/Status register:
        # D7         D6         D5         D4         D3         D2         D1         D0
        # TO_DIS     RES1       RES2       reserved   ALRT_STAT  THI        TLOW       DAV
        #
        # as we see above: Bit 5 + 6 are responsible for resolution control
        # resolution configuration:
        # 00: 0.25°C/LSB, 11-bit word (10 bits plus Sign)
        # 01: 0.125°C/LSB, 12-bit word (11 bits plus Sign)
        # 10: 0.0625°C/LSB, 13-bit word (12 bits plus Sign)
        # 11: 0.03125°C/LSB, 14-bit word (13 bits plus Sign)
        data = struct.unpack('BB', binaryData)
        return LM73Device.resolveResolution(data)

    @staticmethod
    def getManipulatedResolution(data, resolution):
        if resolution > 3 or resolution < 0:
           raise Exception('Resolution have to be > 0 and < 4. Use the appropriate static values from ResolutionEnum!')

        #we dont want to lose leading zeros because
        #we want to make sure that we are able to set the bits for the resolution
        binaryString='0b'+(data[2:]).zfill(8)
        if resolution == ResolutionEnum.ZERO:
            return LM73Device.setAndGetResponseBinary(binaryString, "0", "0")
        elif resolution == ResolutionEnum.ONE:
           return LM73Device.setAndGetResponseBinary(binaryString, "0", "1")
        elif resolution == ResolutionEnum.TWO:
            return LM73Device.setAndGetResponseBinary(binaryString, "1", "0")
        elif resolution == ResolutionEnum.THREE:
             return LM73Device.setAndGetResponseBinary(binaryString, "1", "1")


    @staticmethod
    def setAndGetResponseBinary(data,res1,res0):
        """
            Sets the Resolution1 and Resolution0 Bit
        """
        i=0
        newBinary=''
        while i< len(data):
            if i!= 4 and i!= 5:
                newBinary+=data[i]
            elif i== 4:
                newBinary+=res1
            elif i== 5:
                newBinary+=res0
            i+=1
        pass
        return bin(int(newBinary,2))#convert String back to binary


    @staticmethod
    def checkIfEvenOrOdd(value):
        if (value & 1) != 0:
            return 1
        return 0


    @staticmethod
    def resolveResolution(data):
        """
        Return Values:
        0 for 0.25°C/LSB, 11-bit word (10 bits plus Sign)
        1 for 0.125°C/LSB, 12-bit word (11 bits plus Sign)
        2 for 0.0625°C/LSB, 13-bit word (12 bits plus Sign)
        3 0.03125°C/LSB, 14-bit word (13 bits plus Sign)
        """
        a = struct.unpack('B', data)
        fourBits = (a[0] >> 4) #max. 4 Bits set

        res = LM73Device.checkIfEvenOrOdd(fourBits)

        threeBits = (fourBits >> 1)#eliminate lsb
        res2 = LM73Device.checkIfEvenOrOdd(threeBits)

        if res2 == 1:# we have to increment if this bit is set
            res+=1

        return res+res2



    @staticmethod
    def create_temperature(msb, lsb):
        tmp = float(int(((msb & 0x7F) << 1) | (lsb >> 7)))
        ii = 1
        mask = 0x40

        while ii <= 5:
            if ((lsb & mask) >> (7 - ii)) != 0:
                tmp = tmp + (1.0 / (2 ** ii))
            mask = mask >> 1
            ii = ii + 1

        if (msb & 0x80) != 0:
            tmp = tmp * -1

        return tmp

"""
    This class represents enum-like values. These values are the possible resolution values for our Sensor!
    @see: getManipulatedResolution
"""
class ResolutionEnum:
    ZERO,ONE,TWO,THREE=range(4)

