'''
Created on 04.05.2013

@author: Helmut Kopf
'''

import libthermalraspi.network.tempserver

import unittest
import socket
import os

TEST_REQUEST = """<?xml version="1.0" encoding="utf-8"?>
<request id="$(id)" from="$(from)" to="$(to)"></request>"""

class TempServerTest(unittest.TestCase):
    """
    This test requires a TempServer running in testmode.
    Start the server without start-arguments: Use Start Testserver.bat in the
    network package to start the server in right mode under windows!
    """
    def test__temp_server(self):
        sid = "get_samples"
        sf = "2013-04-30 08:03:34"
        st = "2013-04-30 09:19:52"        
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((libthermalraspi.network.tempserver.DEFAULT_HOST, libthermalraspi.network.tempserver.DEFAULT_PORT))
        sock.sendall(TEST_REQUEST.replace("$(id)", sid).replace("$(from)", sf).replace("$(to)", st).encode('UTF-8'))            
        data = sock.recv(4096)
        sock.close()
        print(data)
        pathToMockXml = os.path.join(os.path.dirname(__file__),os.pardir, 'unittests','resources')
        print(pathToMockXml)
        file = open(pathToMockXml+os.sep+'measurement.xml','r')
        expected = file.read()
        print(expected)
        file.close()        
        self.assertEqual(data, expected.replace("$(id)", sid).replace("$(from)", sf).replace("$(to)", st).encode('UTF-8'))

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TempServerTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
