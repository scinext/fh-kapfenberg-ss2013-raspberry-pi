#!/usr/bin/python

from libthermalraspi.sensors.lm73 import LM73
import os
import time

# create LM73 object with the bus and device-address
dev1 = LM73(1, 0x48)
dev2 = LM73(1, 0x49)

# loopcounter
run = 1
temp_sum = 0
temp_avg = 0
while True:
        temp1 = dev1.get_temperature()
	temp2 = dev2.get_temperature()
        temp_avg = (temp1+temp2)/2
	temp_sum += temp_avg
        os.system('clear')
        print '############# I2C Temp Device #############'
        print '#                                         #'
        print '#     Temperatur-1   ( %05d' % run,'):  ', temp1, '   #'
	print '#     Temperatur-2   ( %05d' % run,'):  ', temp2, '   #'
	print '#     Temperatur-AVG ( %05d' % run,'):  ', temp_avg, '   #'
        print '#     Durchschnittstemperatur :  ', round(temp_sum/run,1), '   #'
        print '#                                         #'
        print '###########################################'
        time.sleep(1)
        run += 1
