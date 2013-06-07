'''
Created on May 11, 2013

@author: group 2 - team pflegp, prutsm, steinb, winste
'''
import os
from libthermalraspi.sensors.lm73device import LM73Device
from libthermalraspi.sensors.ad7414 import AD7414Thermometer
from libthermalraspi.sensors.tc74 import TC74Thermometer
from libthermalraspi.sensors.hyt221 import Hyt221
from libthermalraspi.sensors.simulation import CyclicThermometer
from libthermalraspi.sensors.thermo_proxy_itmG2 import ThermoProxy_ItmG2

class SensorConfigReader(object):
    def __init__(self, filePath ):
        self._filePath = filePath
        
    def read(self):
        return eval( file( self._filePath ).read(), { 'LM73'   : LM73Device
                                                      ,'AD7414' : AD7414Thermometer
                                                      ,'TC74'   : TC74Thermometer
                                                      ,'Hyt221' : Hyt221
                                                      ,'Cyclic' : CyclicThermometer
                                                      ,'ProxyITMG2': ThermoProxy_ItmG2
                                                      } )
