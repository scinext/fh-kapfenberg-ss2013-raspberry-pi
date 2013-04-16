import os
import smbus

class SMBusDevice(object):    
    def __init__(self, busno, addr):
        self.__bus = smbus.SMBus(busno)
        self.__addr = addr
        
    # todo: implement some read/write functions...