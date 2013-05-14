import sys, socket, threading

class ThermoProxy:
    """Connects with a server"""
    
    def __init__(self, host="localhost", port=1234):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._sock.connect((host, port))
        except:
            print("No connection possible!")

    def start(self):
        print("Client started...")
        Connection(self._sock).start()
        #self._sock.close()
    
    def send_msg(self, msg):
        self._sock.send(msg)

    def receive_msg(self):
        return self._sock.recv(1024)

class Connection(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self._server = self.conn.getpeername()[0] + ":" + str(self.conn.getpeername()[1])
        print("Server %s connected..." % (self._server)) 
        
    def run(self):
            data = self.conn.recv(1024)
            print("%s" % (data))

HOST = "10.63.26.24"
PORT = 1024

if (len(sys.argv) > 1):
    HOST = sys.argv[1]
if (len(sys.argv) > 2):
    PORT = int(sys.argv[2])

if __name__ == '__main__':
    tp = ThermoProxy(HOST, PORT)
    tp.start()
    
    # Send example data
    #tp.send_msg('HELP')
    #print(tp.receive_msg)
    #tp.send_command('GET_TEMP')
    #tp.send_command('BYE')
    #for i in range(1, 11):
    #    print("Value %d: %s degree C" % (i, tp.send_command('GET_TEMP')))
    #tp.send_command('BYE')