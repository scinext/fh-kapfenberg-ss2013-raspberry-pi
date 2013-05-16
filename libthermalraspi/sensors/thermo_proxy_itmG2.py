from thermometer import Thermometer
import socket

class ThermoProxy_ItmG2(Thermometer):

    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 7000

    def get_temperature(self):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.connect((self.__host, self.__port))
        self.send_msg('get_temperature')
        return self.__s.recv(1024)

    def send_msg(self, msg):
        return self.__s.send(msg)
