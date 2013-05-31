'''
Created on May 11, 2013

@author: group 2 - team pflegp, prutsm, steinb, winste
'''

from libthermalraspi.services.SensorConfigReader import SensorConfigReader 
import unittest
import tempfile

class SensorConfigReaderTest(unittest.TestCase):

    def setUp(self):
        # create config file that will be used during the test. this
        # way we can get entirely rid of persistent data.
        self.__cfg = tempfile.NamedTemporaryFile()
        self.__cfg.write("""
{ 
  'th-links-oben' : LM73	(1, 49, True),
  'th-links-mitte': AD7414(2, 88, True),
  'th-links-unten': TC74	(3, 46, True),
  'hy-rechts-oben': Hyt221(4, 50, True) 
}
""")
        self.__cfg.flush()
        pass

    def tearDown(self):
        pass
    
    def test_read(self):
        configurationDict = {}
        config = SensorConfigReader(self.__cfg.name).read()
        
        for key in config:
            configurationDict[key] = config[key].__class__.__name__
            
        referenceDict = {'th-links-mitte' : 'AD7414Thermometer',
                         'th-links-oben'  : 'LM73Device',
                         'th-links-unten' : 'TC74Thermometer',
                         'hy-rechts-oben' :  'Hyt221'}
        
        self.assertDictEqual(configurationDict, referenceDict,'Sensor configuration-file-dict and test-dict are different!')
        
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(SensorConfigReaderTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
