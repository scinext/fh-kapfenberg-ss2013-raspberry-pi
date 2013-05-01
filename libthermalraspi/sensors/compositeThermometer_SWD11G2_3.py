from thermometer import Thermometer
import os

class CompositeThermometer(Thermometer):
    __sensors = []
    
    def __init__(self, sensors=[]):
        self.add_sensors(sensors)
 
    def add_sensors(self, sensors):
        self.__sensors.extend(sensors)
        
    def get_temperature(self):
        imTheFather = True
        children = []
        temperatures = []
        pipein, pipeout = os.pipe()
        for sensor in self.__sensors:
            child = os.fork()
            if child:
                children.append(child)
            else:
                imTheFather = False
                os.close(pipein)
                os.write(pipeout, str(sensor.get_temperature()) + "\n")
                os.close(pipeout)
                os._exit(0)
        
        if imTheFather:
            pipein_file = os.fdopen(pipein)
            for child in children:
                os.waitpid(child, 0)
                temperatures.append(pipein_file.readline())
            temperatures = map(float, temperatures)
            return sum(temperatures) / len(temperatures)
