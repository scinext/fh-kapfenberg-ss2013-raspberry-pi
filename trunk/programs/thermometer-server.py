#! /usr/bin/python

import socket, sys

HOST = "localhost"
PORT = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1)

while True:
	conn, addr = sock.accept()
	print "Connected to something"
	
	data = ""
	while data != "BYE":
		data = conn.recv(1024)
		print(data)
	
	conn.close()
	print("Connection closed")

