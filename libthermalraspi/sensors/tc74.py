#!/usr/bin/python
from thermometer import Thermometer
from libthermalraspi.i2c_device import I2CDevice
import struct

class TC74Thermometer (I2CDevice, Thermometer):

	def get_temperature(self):

# "temperature register" according to datasheet (DS)
#response of  TC74 is only one byte, no bits must be shifted.

		self.write('\x00')
		self.write('')

#Attention it doesn't works with sending a 0-Byte. You must send a empty Datapackage (Adress + no data) 
		tByte = self.read(1)
		tRaw = struct.unpack('B', tByte)[0]

#accounting of the temperature based on the temperature table.
		temp = tRaw
		if(tRaw > (0,127)):
			    temp = ((0,255) - tRaw) * (-1)
		return temp
