from thermometer import Thermometer
import socket

class ThermoProxy_ItmG2(Thermometer):
	
	def __init__(self, host, port):
		self.__host = host
		self.__port = port
           
            
	def est_conn(self):
		self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__s.connect((self.__host, self.__port))
		
    def start(self):
        Connection(self._s).start()
        
    def close(self):
        self._s.close()
    
    def send_msg(self, msg):
        return self._s.send(msg)
        
		
		
		
