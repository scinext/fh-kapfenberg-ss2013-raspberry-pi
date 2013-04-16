from libthermalraspi.sensors.thermometer import Thermometer

class HybridSensor(Thermometer):
    
    def get_humidity(self):
        assert False, 'abstract'
        return 0
    
