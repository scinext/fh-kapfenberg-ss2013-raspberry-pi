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
        # select Control/Status register
        self.write('\x04')
        raise Exception('Not yet imlemented')

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
    def checkIfEvenOrOdd(value):
        if (value & 1) != 0:
            return 1
        return 0


    @staticmethod
    def resolveResolution(data):
        """
        Return Values:
        0: 0.25°C/LSB, 11-bit word (10 bits plus Sign)
        1: 0.125°C/LSB, 12-bit word (11 bits plus Sign)
        2: 0.0625°C/LSB, 13-bit word (12 bits plus Sign)
        3: 0.03125°C/LSB, 14-bit word (13 bits plus Sign)
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
