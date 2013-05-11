'''
Created on May 11, 2013

@author: group 2 - team pflegp, prutsm, steinb, winste
'''

from libthermalraspi.services.SensorConfigReader import SensorConfigReader 
import unittest

class SensorConfigReaderTest(unittest.TestCase):
    
    def test_read(self):
        configurationDict = {}
        config = SensorConfigReader('testSensorConfig.cfg').read()
        
        for key in config:
            configurationDict[key] = config[key].__class__.__name__
            
        referenceDict = {'th-links-mitte' : 'AD7414Thermometer',
                         'th-links-oben'  : 'LM73Device',
                         'th-links-unten' : 'TC74Thermometer',
                         'hy-rechts-oben' :  'Hyt221'}
        
        self.assertDictEqual(configurationDict, referenceDict,'Sensor configuration-file-dict and test-dict are different!')
        
        