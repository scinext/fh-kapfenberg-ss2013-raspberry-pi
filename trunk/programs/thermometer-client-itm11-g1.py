import sys, socket, threading

class ThermoProxy():
    """Connects with a server"""
    
    def __init__(self, host="127.0.0.1", port=1024):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._sock.connect((host, port))
            server = self._sock.getpeername()[0] + ":" + str(self._sock.getpeername()[1])
            print("%s connected" % (server));
        except:
            print("Can not reach server.")
    
    def send_msg(self, msg):
        self._sock.send(msg)

    def receive_msg(self):
        return self._sock.recv(1024)

if __name__ == '__main__':
    default = "127.0.0.1:1024"
    host_str = raw_input("<HOST>:<PORT> [%s] " % (default))
    
    # use default address if not specified
    if (host_str == ''):
        host_str = default
    
    host_str_array = host_str.split(":")
    
    # use specified host address
    HOST = host_str_array[0]
    
    if len(host_str_array) > 1:
        # use specified port
        PORT = int(host_str_array[1])
    else:
        # use default port
        PORT = int(default.split(":")[1])
    
    tp = ThermoProxy(HOST, PORT)
    print(tp.receive_msg())
    
    while True:
        cmd = raw_input("client# ")
        tp.send_msg(cmd.upper())
        print(tp.receive_msg())