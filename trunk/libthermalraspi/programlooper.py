import time
import sys
import signal

class ProgramLooper:
    def __init__(self, interval_seconds):
        self.__interval = interval_seconds
        self.__counter = 0

        # to be set from signal handler
        self.__stop = False
        
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGQUIT, self.signal_handler)
        
    def __iter__(self):
        while not self.__stop:
            yield self.__counter
            self.__counter += 1
            time.sleep(self.__interval)
            
            
    def signal_handler(self, signal, frame):
        print("Shutdown application")
        self.__stop = True
