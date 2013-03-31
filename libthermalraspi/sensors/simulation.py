from thermometer import Thermometer

import itertools

class CyclicThermometer(Thermometer):
    def __init__(self, temperatures):
        self.__temperatures = itertools.cycle(temperatures)
        pass

    def getTemp(self):
        return self.__temperatures.next()

    pass
