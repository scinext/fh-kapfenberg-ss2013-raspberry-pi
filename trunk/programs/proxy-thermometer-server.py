#! /usr/bin/python

import socket, sys, threading

# import drivers
import libthermalraspi.sensors.stds75
import libthermalraspi.sensors.lm73device
import libthermalraspi.sensors.simulation

class SocketServer():
	
	def __init__(self, host, port, thermometer):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((host, port))
		self.sock.listen(1)
		self.thermometer = thermometer

	def start(self):
		print("Temperature Server started...")
		
		while True:
			conn, _ = self.sock.accept()
			ClientConnection(conn, self.thermometer).start()
			
		self.sock.close() # TODO: define some break condition

class ClientConnection(threading.Thread):

	def __init__(self, conn, thermometer):
		threading.Thread.__init__(self)
		self.conn = conn
		self.thermometer = thermometer
		
	def run(self):
			client = self.conn.getpeername()[0] + ":" + str(self.conn.getpeername()[1])
			
			print(client + " connected") 
			self.conn.sendall("Welcome to the Raspberry Pi thermometer server!\nType HELP for a list of available commands.\n")
			
			data = ""  # init data
			while "BYE" not in data:
				data = self.conn.recv(1024)
				
				if len(data) == 0:
					break
				
				print(client + ": " + data)
					
				if "HELP" in data:
					self.conn.sendall("====== COMMANDS ======\nHELP\nGET_TEMP\nBYE")
				elif "GET_TEMP" in data:
					print("Temperature data requested by " + client + ". Sending...")
					self.conn.sendall(str(self.thermometer.get_temperature()))  # send actual data
				elif "EMPTY" in data:
					self.conn.sendall(" ")
				elif "BYE" in data:
					pass
				else:
					self.conn.sendall("Command not found")
			
			self.conn.close()
			print(client + " closed connection")
			
		
HOST = sys.argv[1]
PORT = int(sys.argv[2])

#get driver from config file
# demo-config-file: STDS75(0, 0x4e)
DRIVER = eval(file(sys.argv[3]).read(), {'STDS75': libthermalraspi.sensors.stds75.Stds75,
                                         'LM73': libthermalraspi.sensors.lm73device.LM73Device,
                                         'Cyclic': libthermalraspi.sensors.simulation.CyclicThermometer})

if __name__ == '__main__':
    server = SocketServer(HOST, PORT, DRIVER)
    server.start()

