from thermometer import Thermometer
import os

# SWD11 - G2 - 2 - Pflegpeter, Prutsch, Steinbauer, Winkler
class CompositeSensor(Thermometer):
    __sensors = []
    
    def __init__(self, sensors=[]):
        self.add_sensors(sensors)
    
    def add_sensors(self, sensors):
        self.__sensors.extend(sensors)
    
    def get_temperature(self):
        child_ids = dict()
        pipes = dict()
        for index, item in enumerate(self.__sensors):
            parentRead, childWrite = os.pipe()
            # fork a child process
            child = os.fork()
            # os.fork(): Return 0 to child process and PID of child to parent process.
            if (child == 0):
                # write some formatted temp stuff in the pipe
                os.write(childWrite, str(item.get_temperature()).zfill(7))
                os._exit(0)
            else:
                # save the pid of all childs
                child_ids[index]=child
                pipes[index]=parentRead
                # close not used filedescriptor
                os.close(childWrite)
        
        temperatures = []
        for _ in child_ids:
            # wait for any child to return
            pid, _ = os.wait()
            # find child-pid in the dictionary to save corresponding temp
            for index,cid in child_ids.items():
                if (cid == pid):
                    # read exact 7 bytes from pipe
                    temp = os.read(pipes[index],7)
                    temperatures.append(float(temp))
                    '''print("%s with pid(%s) sent: %3.3f" % (index,cid,float(temp)))'''
        return sum(temperatures) / len(temperatures)


