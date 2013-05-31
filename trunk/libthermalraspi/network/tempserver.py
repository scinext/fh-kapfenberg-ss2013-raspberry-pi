'''
Created on 04.05.2013

@author: Helmut Kopf
'''

import socket
import threading
import logging
import os
import sys
import datetime
import platform
from xml.dom.minidom import parseString

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 1234

tempServer = None

def getDefaultLogFile():
    return os.path.join(os.path.dirname(os.path.abspath( __file__ )), "TempServer.log")


class TempServer(object):
    """
    Temperature server
    """
    def __init__(self, host = "localhost", port = 1234, logfile = getDefaultLogFile(), loglevel = logging.INFO, testmode = False):
        self.__sock = None
        self.__host = host
        self.__port = port
        self.__logger = TempServer.__createLogger(logfile, loglevel)
        self.__testmode = testmode
        self.__logger.info("Server initialized: Host = %s, Port = %s" % (host, port))
        self.__handlers = []
        self.__lock = threading.Lock()      

    def start(self):
        try:
            print("Server startet at " + str(datetime.datetime.now()) + "...")
            self.__logger.info("Server startet...")

            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.bind((self.__host, self.__port))
            self.__sock.listen(1)

            while True:
                conn, _ = self.__sock.accept()
                print("new connection accepted at " + str(datetime.datetime.now()) + "...")
                handler = ResponseHandler(conn, self.__removeHandler, self.__logger, self.__testmode)
                self.__handlers.append(handler)
                handler.start()

        except socket.error as e:
            self.__logger.exception("Socket error: %s" % e)
        except socket.herror as e:
            self.__logger.exception("Socket address error: %s" % e)
        except socket.timeout as e:
            self.__logger.exception("Socket timeout error: %s" % e)
        except Exception as e:
            self.__logger.exception("Unexpected server error: %s" % e)
        finally:
            if self.__sock != None:
                self.__sock.close()
            self.__logger.info("Server stopped...")
            print("Server stopped at " + str(datetime.datetime.now()) + "...")
            
    def dispose(self):
        try:
            self.__logger.info("Server handling signal termination at " + str(datetime.datetime.now()) + "...")
            for handler in self.__handlers:
                handler.join()                                       
            self.__logger.info("Signal termination handling done")
        except Exception as e:
            self.__logger.exception("Server handling signal termination failed: %s" %e)
            
    def __removeHandler(self, handler):                    
        try:
            self.__lock.acquire()                       
            self.__handlers.remove(handler)            
            self.__logger.info("Handler successfully removed!")
        except ValueError as e:            
            self.__logger.exception("Remove handler failed: %s" %e)
        except Exception as e:
            self.__logger.exception("Remove handler failed: %s" %e)
        finally:
            self.__lock.release()
            
    @staticmethod
    def __createLogger(logfile, level = logging.INFO):
        logger = logging.getLogger("tempserver")
        fhdlr = logging.FileHandler(logfile)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fhdlr.setFormatter(formatter)
        logger.addHandler(fhdlr)
        logger.setLevel(level)
        return logger

class ResponseHandler(threading.Thread):
    def __init__(self, connection, donecallback, logger, testmode = False):
        threading.Thread.__init__(self)
        self.__connection = connection
        self.__donecallback = donecallback
        self.__logger = logger
        self.__testmode = testmode
        self.__logger.info("Request handler invoked: Testmode = " + str(self.__testmode))

    def run(self):
        try:
            self.__logger.info("Response requested...")

            (sid, sdtf, sdtt) = self.__getDateRange()
            if self.__testmode == True:
                pathToMockXml = os.path.join(os.path.dirname(__file__),os.pardir, 'unittests','resources')
                file = open(pathToMockXml+os.sep+'measurement.xml','r')
                data = file.read()
                file.close()
                #dom = parseString(data)
                self.__connection.send(data.replace("$(id)", sid).replace("$(from)", sdtf).replace("$(to)", sdtt).encode('UTF-8'))
            else:
                # todo...
                pass

        except Exception as e:
            self.__logger.exception("Response failed by an unexpected error: %s" % e)
        finally:
            self.__connection.close()
            self.__donecallback(self)

    def __getDateRange(self):
        xml = self.__getXml()

        if xml != None:
            xi = xml.documentElement.getAttributeNode('id')
            xf = xml.documentElement.getAttributeNode('from')
            xt = xml.documentElement.getAttributeNode('to')
            self.__logger.info("id = " + xi.nodeValue + ", from = " + xf.nodeValue + ", to = " + xt.nodeValue)
            return (str(xi.nodeValue), str(xf.nodeValue), str(xt.nodeValue))
        else:
            self.__logger.info("Xml is null!")
        return ""


    def __getXml(self):
        xmlstr = self.__connection.recv(1024)

        if len(xmlstr) > 0:
            xml = parseString(xmlstr)
            return xml
        return None
    
def addSignalHandler():
    if platform.system() != "Windows":
        import signal
        signal.signal(signal.SIGINT, terminationHandler)
        signal.signal(signal.SIGTERM, terminationHandler)
        print("Signal handler successfully installed")                        

def terminationHandler(signal, frame):
    try:
        print("Server termination signal handled at " + str(datetime.datetime.now()) + "...")
        if tempServer != None:
            tempServer.dispose()      
    finally:
        sys.exit(0)            

if __name__ == '__main__':
    host = DEFAULT_HOST = "localhost"
    port = DEFAULT_PORT = 1234
    testmode = False

    if len(sys.argv) >= 2:
        host = str(sys.argv[1])
        if len(sys.argv) >= 3:
            port = int(sys.argv[2])
            if len(sys.argv) >= 4:
                testmode = int(sys.argv[3]) != 0

    addSignalHandler()
    tempServer = TempServer(host, port, getDefaultLogFile(), logging.INFO, testmode)
    tempServer.start()
