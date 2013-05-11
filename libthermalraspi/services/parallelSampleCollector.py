# coding: utf-8
from libthermalraspi.services.sampleCollector import SampleCollector

import datetime
import os

class ParallelSampleCollector(SampleCollector):
        
    def __init__(self, store, sensorList):
        __store = store
        if type(sensorList) is dict:
            __sensorList = sensorList
        else:
            print "Parameter sensorList ist kein Dictionary"
        pass
 
    def run(self, looper):
        """Messungen starten und per externem iterierbarem Objekt
        (looper) Intervall der Messzyklen festlegen.
        
        @param looper: Iterierbares Objekt/List/...
        """
        for i in looper:
            yield i
            self.__getAllSensorTemperatures()
        pass
    
    def __getAllSensorTemperatures(self):
        imTheFather = True
        children = {}   #dictionary sensorName:childPid
        pipein, pipeout = os.pipe()
      
        for sensorName, sensorInstance in self.__sensorList.items():
            child = os.fork()
            if child:
                children[sensorName] = child
            else:
                imTheFather = False
                os.close(pipein)
                
                try:
                    returnValue = {'temp' : float(sensorInstance.get_temperature()) }
                except IOError as e:
                    #self.__logger.exception("Sensor IOError: %s" % e)
                    returnValue = {'errorCode' : 1}
                    pass
                os.write(pipeout, str(returnValue))
                
                os.close(pipeout)
                os._exit(0)

        if imTheFather:
            sensorDict = eval(os.fdopen(pipein), {'temp' : 0.0, 'errorCode' : 0} )
            for sensorName, childPid in children.items():
                os.waitpid(childPid, 0)
                
                'Persistiere Messdaten in DB'
                self.__store.add_sample(datetime.datetime.now(), sensorName, sensorDict['temp'], sensorDict['errorCode'])
                
        pass
