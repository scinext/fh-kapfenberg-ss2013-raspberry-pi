from libthermalraspi.i2c_device import I2CDevice

import time
import struct

class LM73(I2CDevice):
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    def get_temperature(self):
        # request temperature
        self.write('\x00')
        # read temperature - 2 Bytes
        result = self.read(2)
	b1, b2 = struct.unpack('bb', result)
	# shift first byte one position to the left and second 3 to the right
	# &15 and | are used for binary addition of the two bytes
	Traw = ((b1 & 15) << 1) | ((b2 & 15) >> 3)
	return float(Traw)
