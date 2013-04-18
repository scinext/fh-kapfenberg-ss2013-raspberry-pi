#! /usr/bin/python

import sys, socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 7000))

serversocket.listen(5)
print("Waiting for connections")

while 1:
    (clientsocket, address) = serversocket.accept()

    print("Received connection")
    
    data = ""
    while data != "exit":
        data = clientsocket.recv(1024)
        print(data)
    
    clientsocket.close()
    print("Connection closed")