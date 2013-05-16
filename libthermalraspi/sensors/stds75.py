""" Author: Christopher Barilich - ITM11 """


import struct
from libthermalraspi.i2c_device import I2CDevice
from libthermalraspi.sensors.thermometer import Thermometer


class Stds75(I2CDevice, Thermometer):
    '''
    Thermal Senser STDS75

    default resolution for thermometer is 9 bit (.5)
    '''
    def __init__(self, bus, addr):
        I2CDevice.__init__(self, bus, addr)

    
    def get_temperature(self):
        
	"""
	returns the current temperature
	if polled too frequently, sensor wont update the temperature register
	update cycles in ms:
	    9 bit:	 150ms
	   10 bit:	 300ms
	   11 bit:	 600ms
	   12 bit:	1200ms

	negative values not yet implemented!
	"""

	# get current resolution

	conf = self.read_config()
	mask = 0x60  # 0110 0000
	res = conf & mask  # extract resolution from config register
	# get temperature from register
        
        self.write('\x00')
        data = self.read(2)
        t_raw = struct.unpack('>h', data)
	t_raw = t_raw[0]

#	msb = 0b11110101
#	lsb = 0b11100000
#	data = struct.pack('BB', msb, lsb)
 #       t_raw = struct.unpack('>h', data)
#	t_raw = t_raw[0]
#	print t_raw
	
        # return  t_raw
	# t_raw = ((msb << 8) + lsb)  # convert to 2 Byte Integer

	if (res == 0x00):  # 9 bit resolution 0.5 degree
	    print "res: 0.5"
	    return (t_raw >> 7) * 0.5

	if (res == 0x20):  # 10 bit resolution 0.25 degree
	    print "res: 0.25"
	    return (t_raw >> 6) * 0.25

	if (res == 0x40):  # 11 bit resolution 0.125 degree
	    print "res: 0.125"
	    return (t_raw >> 5) * 0.125

	if (res == 0x60):  # l2 bit resolution 0.0625 degree
	    print "res: 0.0625"
	    return (t_raw >> 4) * 0.0625


        
    def read_config(self):
	'''
	read config from config register
	returns 1Byte integer
	see Datasheet for details
	'''
	self.write('\x01')
	data = self.read(1)
	conf = struct.unpack('B', data)
	return (conf[0])


    def set_resolution(self, res=12):
        '''
        set resolution in bits: 9, 10, 11, 12 (default) and write to config register
        '''
	if (res < 9 or res > 12):
	    raise Exception('Incorrect resolution! set it to 9, 10, 11 or 12')

	# reset the resolution bits to 0
	oldconf = self.read_config()
	reset_mask = 0x9F  # 10011111 
	resetted_res = oldconf & reset_mask
	    
	# set the new resolution (6th and 7th bit)
	if (res == 9):
	    new_conf = resetted_res | 0x00  # 0000 0000

	if (res == 10):
	    new_conf = resetted_res | 0x20  # 0010 0000

	if (res == 11):
	    new_conf = resetted_res | 0x40  # 0100 0000

	if (res == 12):
	    new_conf = resetted_res | 0x60  # 0110 0000
	
	self.write_config(new_conf)

    def write_config (self, data):
	''' write data to config register '''
	self.write(struct.pack('BB', 1, data))  # first byte: register, second byte: values


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
