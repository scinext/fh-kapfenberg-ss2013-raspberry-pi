'''
Created on 29.04.2013

@author: Patrick Groeller
'''

from xml.dom import minidom
from databaseaccess.Measurement import Measurement


class XmlMeasurementService:

    def __init__(self, listOfMeasurements):
        self.__listOfMeasurements = listOfMeasurements


    def toXml(self):
        doc = minidom.Document()
        root = doc.createElement("response")
        doc.appendChild(root)

        root.setAttribute('id',"$(id)")
        root.setAttribute('from',"$(from)")
        root.setAttribute('to',"$(to)")

        sensors = doc.createElement('sensors')
        root.appendChild(sensors)
        for measurement in self.__listOfMeasurements:
            #if type(measurement) is Measurement:
            sensor = doc.createElement('sensor')
            sensors.appendChild(sensor)
            sensor.setAttribute('name',measurement.getSensorname())
            sensor.setAttribute('value',str(measurement.getMeasureVal()))
            sensor.setAttribute('timestamp',str(measurement.getTimestamp()))
            sensor.setAttribute('errorCode',str(measurement.getErrorCode()))

        #print doc.toprettyxml(encoding='utf-8')
        return doc.toprettyxml(encoding='utf-8')
        pass
