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
