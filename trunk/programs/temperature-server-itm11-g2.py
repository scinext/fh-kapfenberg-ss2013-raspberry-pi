#! /usr/bin/python

import sys, socket, time, datetime

from libthermalraspi.sensors.simulation import CyclicThermometer
from libthermalraspi.sensors.stds75 import Stds75

## th = CyclicThermometer([1, 2.5, 3])
th = Stds75(1, 0x4e)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 7000))

serversocket.listen(5)
print("Waiting for connections")

while 1:
    (clientsocket, address) = serversocket.accept()

    print("Received connection")

    data = ""
    while "QUIT" not in data:
        data = clientsocket.recv(1024)
        if len(data) == 0:
            break
        if "get_temperature" in data:
            clientsocket.sendall(str(th.get_temperature()) + "\n")
    clientsocket.close()
    print("Connection closed")
