from thermometer import Thermometer

import itertools

class CyclicThermometer(Thermometer):
    def __init__(self, temperatures):
        self.__temperatures = itertools.cycle(temperatures)
        pass

    def get_temperature(self):
        return self.__temperatures.next()

    pass
