#!/usr/bin/python

import sys, socket
from sensors.thermometer import Thermometer

class ThermoProxy(Thermometer):
    """Connects with a server"""
    
    def __init__(self, host="127.0.0.1", port=1024):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self._sock.connect((host, port))
        except:
            raise Exception("Host not found.")
    
    def get_temperature(self):
        self._sock.send("GET_TEMP")
        return self._sock.recv(1024)