# -*- coding: utf-8 -*-

import struct

from libthermalraspi.i2c_device import I2CDevice
from libthermalraspi.sensors.thermometer import Thermometer

# Not yet tested on raspberry
# all methods successfully tested against
# datasheet specs.
class LM73Device(Thermometer, I2CDevice):
    """
    Author: HeKo
    """

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

        newData = LM73Device.getManipulatedResolution(unpackedData[0], resolution)
        self.write(struct.pack('B', newData))

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
        data = struct.unpack('B', binaryData)
        return LM73Device.resolveResolution(data)

    @staticmethod
    def getManipulatedResolution(data, resolution):
        if resolution > 3 or resolution < 0:
            raise Exception('Resolution have to be > 0 and < 4. Use the appropriate static values from ResolutionEnum!')

        resetResMask = 0xCF #11001111
        resetedRes =data & resetResMask

        if resolution == ResolutionEnum.ZERO:
            return resetedRes
        elif resolution == ResolutionEnum.ONE:
            return resetedRes | 0x10 # 0001 0000
        elif resolution == ResolutionEnum.TWO:
            return resetedRes | 0x20 # 0010 0000
        elif resolution == ResolutionEnum.THREE:
            return resetedRes | 0x30 # 0011 0000

    @staticmethod
    def resolveResolution(data):
        """
        Return Values:
        0 for 0.25°C/LSB, 11-bit word (10 bits plus Sign)
        1 for 0.125°C/LSB, 12-bit word (11 bits plus Sign)
        2 for 0.0625°C/LSB, 13-bit word (12 bits plus Sign)
        3 0.03125°C/LSB, 14-bit word (13 bits plus Sign)
        """
        mask=0x30 #00110000
        return(data[0] & mask)>> 4

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
    This class represents enum-like values. These values are the possible resolution values for our sensor!
    @see: getManipulatedResolution
"""
class ResolutionEnum:
    ZERO,ONE,TWO,THREE=range(4)

