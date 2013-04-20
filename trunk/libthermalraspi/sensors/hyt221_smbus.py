from libthermalraspi.smbus_device import SMBusDevice
from libthermalraspi.sensors.thermometer import Thermometer
from libthermalraspi.sensors.humiditysensor import HumiditySensor

import time

class Hyt221SMBus(SMBusDevice, Thermometer, HumiditySensor):
    def __init__(self, bus, addr):
        SMBusDevice.__init__(self, bus, addr)

    def _perform_measurement(self):
        # init -> trigger measurement
        self.__bus.write_quick(self.__addr)
        
        # wait until measurement is completed
        while(self.__bus.read_byte(self.__addr) & 0xC0 != 0): # check status bits
            time.sleep(0.001)

    def get_temperature(self):
        self._perform_measurement()
        
        # read measurement results
        result = bytearray("    ")
        result = self.__bus.read_i2c_block_data(self.__addr, 0)
                
        # calculating temperature -> see datasheet
        result[3] = result[3] & 0x3F
        Traw = result[2] << 6 | result[3]
        T = 165.0 * Traw / (2**14) - 40
        
        return T    
    def get_humidity(self):
        self._perform_measurement()
        
        # read measurement results
        result = bytearray("    ")
        result = self.__bus.read_i2c_block_data(self.__addr, 0)
        
        Hraw = result[0] << 8 | result[1]
        Hraw = Hraw & 0x3FFF
        H = 100.0 * Hraw / (2**14)
        
        return H
