'''
Created on 04.05.2013

@author: Helmut Kopf
'''

import libthermalraspi.network.tempserver

import unittest
import socket

class TempServerTest(unittest.TestCase):
    """
    This test requires a TempServer running in testmode.
    Start the server without start-arguments: Use Start Testserver.bat in the
    network package to start the server in right mode!
    """
    def test__temp_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((libthermalraspi.network.tempserver.DEFAULT_HOST, libthermalraspi.network.tempserver.DEFAULT_PORT))        
        data = sock.recv(4096)
        sock.close()
        print(data)
        self.assertEqual(data, libthermalraspi.network.tempserver.TEST_XML)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TempServerTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
