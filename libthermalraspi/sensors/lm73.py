from libthermalraspi.i2c_device import I2CDevice

import time
import struct

class LM73(I2CDevice):
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    def get_temperature(self):
        # request temperature
        self.write('\x00')
        # read temperature
        return float(struct.unpack('b', self.read(1))[0])
