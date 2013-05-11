from thermometer import Thermometer
from libthermalraspi.i2c_device import I2CDevice

import struct

class HypotheticalThermometer(I2CDevice, Thermometer):

    def get_temperature(self):
        # select register ("temperature register", according to
        # hypothetical datasheet) for next operation
        self.write('\x00')

        # read 2-byte temperature register, and unpack the bytes into
        # 2 8-bit integers which are then combined to form a floating
        # point number (again according ot datasheet).
        msb_lsb = self.read(2)
        msb, lsb = struct.unpack('BB', msb_lsb)
        return self.__frbozz_hardware_float(msb, lsb)

    @staticmethod
    def __frbozz_hardware_float(msb, lsb):
        return float(((msb << 8) | lsb) >> 4)
