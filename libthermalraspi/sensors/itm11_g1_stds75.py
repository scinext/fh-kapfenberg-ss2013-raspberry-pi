from libthermalraspi.i2c_device import I2CDevice

import time
import struct
import sys

class Stds75(I2CDevice):
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    def get_temperature(self):
        # set register for next operation to 1 (CONF)
        self.write('\1')
        
        # read config
        config = self.read(1)
        config_ = struct.unpack('B', config)[0]
        
        # unset bit 5 and 6 (resolution)
        config_ = config_ & 0b10011111
        
        # set bit 5 and 6 to 1 and 0
        # 00 = 0.5C, 150ms
        # 01 = 0.25C, 300ms
        # 10 = 0.125C, 600ms
        # 11 = 0.0625C, 1200ms
        config_ = config_ | 0b01000000
        
        # write config
        self.write(struct.pack('BB', 1, config_))
        
        # set register for next operation to 0 (TEMP)
        self.write('\0')
        
        # read measurement results
        result = self.read(2)
        b1, b2 = struct.unpack('BB', result)
        
        # convert temperature and return it
        return b1 + (b2 / 256.0)
        
