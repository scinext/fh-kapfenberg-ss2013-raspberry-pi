


import struct
from libthermalraspi.i2c_device import I2CDevice
from libthermalraspi.sensors.thermometer import Thermometer


class Stds75(I2CDevice, Thermometer):
    '''
    classdocs
    '''
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    
    def get_temperature(self):
        
        #select temp register
        
        self.write('\x00')
        data = self.read(2);
        msb, lsb = struct.unpack('BB', data)
        print msb
        print lsb
        
        
        
#        res = 0.0625  #12 bit resolution
#        
#        # if positive value
#
#        x = t_raw = 0b0001100100010000 # 25,0625
#        temp = (x >> 4) * res
#        
#        # if negative value
#        x = t_raw = 0b1111010111100000 #-10,125 
#        x = ~x+1 # twos complement
#        x = x>>4 # remove tailing 0s
#        x = (x - 4096) *-1 * res # remove overflow and multiply with resolution
        
        
      
    