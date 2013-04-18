#! /usr/bin/python

import sys, socket, time, datetime

from libthermalraspi.sensors.simulation import CyclicThermometer
th = CyclicThermometer([1, 2.5, 3])

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 7000))

serversocket.listen(5)
print("Waiting for connections")

while 1:
    (clientsocket, address) = serversocket.accept()

    print("Received connection")

    i = 0
    while i < 1:
        #data = clientsocket.recv(1024)
        ts = time.time()
        clientsocket.sendall(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + ": " + str(th.get_temperature()) + "\n")
        time.sleep(1)
    
    #clientsocket.close()
    #print("Connection closed")