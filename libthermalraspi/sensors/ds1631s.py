from thermometer import Thermometer
from libthermalraspi.i2c_device import I2CDevice

import struct

class DS1631SThermometer(I2CDevice, Thermometer):
    
    def get_temperature(self):
        self.write('\x4F')
        msb_lsb = self.read(2)
        msb, lsb = struct.unpack('BB', msb_lsb)
        return self.__bitshift_to_hardware_float(msb, lsb)

    @staticmethod
    def __bitshift_to_hardware_float(msb, lsb):
	 return msb
	 return float((((msb << 4) | lsb) >> 8  )/4.0)
