from thermometer import Thermometer
from socket import socket

class ThermoProxy (Thermometer):
    def __init__(self, host, port=99999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect(host, port)
        
    def connect(self, host, port):
        self.sock.connect(host, port)
    
    def get_temperature(self):
        return 99.9
    
tp = ThermoProxy('192.168.2.150', 99999)