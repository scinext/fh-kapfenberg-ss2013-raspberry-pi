from thermometer import Thermometer
import socket

class ThermoProxy (Thermometer):
    """Connects with a server, retrieves temperatures and outputs them"""
    
    def __init__(self, host, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(host, port)
        
    def connect(self, host, port):
        try:
            self._sock.connect((host, port))
        except:
            print("No connection possible")
            
    def get_temperature(self):
        MSGLEN = 4096
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self._sock.recv(MSGLEN - len(msg))
            if chunk == '':
                raise RuntimeError("Socket connection broken")
            msg += chunk
        return msg
        
tp = ThermoProxy('192.168.2.138', 5000)

for i in range(1, 11):
    print("Value %d: %s degree C" % (i, tp.get_temperature()))