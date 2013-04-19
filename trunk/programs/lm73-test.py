#!/usr/bin/env python

from libthermalraspi.sensors.lm73 import LM73
import os
import time

# create LM73 object with the bus and device-address
dev1 = LM73(1, 0x48)

# loopcounter
run = 1
temp_sum = 0
while True:
        temp = dev1.get_temperature()
        temp_sum += temp
        os.system('clear')
        print '############# I2C Temp Device #############'
        print '#                                         #'
        print '#     Temperatur ( %05d' % run,'):     ', temp, '    #'
        print '#     Durchschnittstemperatur:  ', round(temp_sum/run,1), '    #'
        print '#                                         #'
        print '###########################################'
        time.sleep(1)
        run += 1
