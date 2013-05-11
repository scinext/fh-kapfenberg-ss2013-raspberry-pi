from libthermalraspi.i2c_device import I2CDevice
from libthermalraspi.sensors.thermometer import Thermometer
from libthermalraspi.sensors.humiditysensor import HumiditySensor

import time
import struct

class Hyt221(I2CDevice, Thermometer, HumiditySensor):

    def _perform_measurement(self):
        # init -> trigger measurement
        self.write('')
        
        # wait until measurement is completed
        status = struct.unpack('B', self.read(1))
        while(status[0] & 0xC0 != 0): # check the status bits
            time.sleep(0.001)
            status = struct.unpack('B', self.read(1))

    def get_temperature(self):
        self._perform_measurement()
        
        # read measurement results
        result = self.read(4)
        _, _, b2, b3 = struct.unpack('BBBB', result)
        
        # calculating temperature -> see datasheet
        b3 = b3 & 0x3F
        Traw = b2 << 6 | b3
        T = 165.0 * Traw / (2**14) - 40
        
        return T    
    def get_humidity(self):
        self._perform_measurement()
        
        # read measurement results
        result = self.read(2)
        b0, b1 = struct.unpack('BB', result)
        
        Hraw = b0 << 8 | b1
        Hraw = Hraw & 0x3FFF
        H = 100.0 * Hraw / (2**14)
        
        return H
    
