'''
Created on 29.04.2013

@author: Patrick Groeller
'''

from xml.dom import minidom
from libthermalraspi.database.Measurement import Measurement


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
        responseStatus = doc.createElement('status')
        root.appendChild(responseStatus)

        try:
            sensors = doc.createElement('samples')
            root.appendChild(sensors)
            for measurement in self.__listOfMeasurements:
                sensor = doc.createElement('sample')
                sensor.setAttribute('sensorname',measurement.getSensorname())
                sensor.setAttribute('temperature',str(measurement.getMeasureVal()))
                sensor.setAttribute('timestamp',str(measurement.getTimestamp()))
                sensor.setAttribute('status',str(measurement.getErrorCode()))
                sensors.appendChild(sensor)

            responseStatus.setAttribute('error','ok')
        except Exception as e:
            responseStatus.setAttribute('error','overflow')


        #print doc.toprettyxml(encoding='utf-8')
        return doc.toprettyxml(encoding='utf-8')
        pass
