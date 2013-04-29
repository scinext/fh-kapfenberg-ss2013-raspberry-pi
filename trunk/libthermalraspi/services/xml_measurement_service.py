from xml.dom import minidom
from databaseaccess.Measurement import Measurement

class XmlMeasurementService:

    def __init__(self, listOfMeasurements):
        self.__listOfMeasurements = listOfMeasurements


    def toXml(self):
        doc = minidom.Document()
        root = doc.createElement("response")
        doc.appendChild(root)
        for measurement in self.__listOfMeasurements:
            #if type(measurement) is Measurement:
            item = doc.createElement('item')
            root.appendChild(item)
            item.setAttribute('name',measurement.getSensorname())
            item.setAttribute('value',str(measurement.getMeasureVal()))
            item.setAttribute('timestamp',str(measurement.getTimestamp()))
            item.setAttribute('errorCode',str(measurement.getErrorCode()))

        #print doc.toprettyxml(encoding='utf-8')
        return doc.toprettyxml(encoding='utf-8')
        pass