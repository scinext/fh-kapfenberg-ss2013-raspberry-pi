from libthermalraspi.services.xml_measurement_service import XmlMeasurementService
from xml.dom.minidom import parseString

import sys,os
import unittest

class XmlMeasurementServiceTest(unittest.TestCase):
    def test_toXml(self):
        file = open(os.path.dirname(__file__)+os.sep+'resources'+os.sep+'test_xmlService'+os.sep+'measurement.xml','r')
        data = file.read()
        file.close()
        dom = parseString(data)
        expectedOutput =dom.toxml(encoding='utf-8')[:38]+ os.linesep + dom.toxml(encoding='utf-8')[38:]+ os.linesep


        dataList =[MockObject(MockSensor("Strawberry"),"2013-04-30 08:03:38",20.12,0),
                   MockObject(MockSensor("Raspberry"),"2013-05-31 09:03:38",30,0),
                   MockObject(MockSensor("Banana"),"2013-04-30 08:03:38",27.132,1),
                   MockObject(MockSensor("Blackberry"),"2013-05-31 09:03:38",27.132,0)]
        xmlService = XmlMeasurementService(dataList)
        self.assertEqual(expectedOutput, xmlService.toXml())
        pass

    def test_toXmlWithFailure(self):
        file = open(os.path.dirname(__file__)+os.sep+'resources'+os.sep+'test_xmlService'+os.sep+'errorMeasurement.xml','r')
        data = file.read()
        file.close()
        dom = parseString(data)
        expectedOutput =dom.toxml(encoding='utf-8')[:38]+ os.linesep + dom.toxml(encoding='utf-8')[38:]+ os.linesep

        xmlService = XmlMeasurementService([""])

        self.assertEqual(expectedOutput, xmlService.toXml())
        pass

suite = unittest.defaultTestLoader.loadTestsFromTestCase(XmlMeasurementServiceTest)

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass

class MockObject:
    def __init__(self,sensor,timestamp,measureVal,errorCode):
        self._sensor = sensor
        self._timestamp = timestamp
        self._measureVal = measureVal
        self._errorCode = errorCode

    def getSensorname(self):
        return self._sensor.getName()

    def getTimestamp(self):
        return self._timestamp

    def getMeasureVal(self):
        return self._measureVal

    def getErrorCode(self):
        return self._errorCode

class MockSensor:
     def __init__(self,name):
         self.__name=name

     def getName(self):
          return self.__name