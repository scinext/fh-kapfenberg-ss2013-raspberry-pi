from thermometer import Thermometer
from libthermalraspi.i2c_device import I2CDevice

import struct

class AD7414Thermometer(I2CDevice, Thermometer):
    
    def get_temperature(self):
        # "temperature register" according to datasheet (DS)
        self.write('\x00')

        # Read 2-byte temperature register, unpack the bytes into
        # two 8-bit integers which are then combined to a floating
        # point number (again according to the DS).
        msb_lsb = self.read(2)
        msb, lsb = struct.unpack('BB', msb_lsb)
        return self.__bitshift_to_hardware_float(msb, lsb)

    @staticmethod
    def __bitshift_to_hardware_float(msb, lsb):
        # 0000 0000 | 0000 0000
        # -- msb -- | -- lsb --
        # needed bits are: 0000 0000 | 00
        
        # To avoid overwriting the msb
        # (most significant byte) with the lsb
        # (least significant byte), the msb
        # must be bit-shifted 8 bits left and
        # be combined with the lsb at the end.
        # Following this, both bytes must be
        # shifted to the proper position as
        # outlined in the DS (cut off the
        # right-most six bits) and perform
        # Temp-Calculation formular.
        return float((((msb << 8) | lsb) >> 6)/4.0)
