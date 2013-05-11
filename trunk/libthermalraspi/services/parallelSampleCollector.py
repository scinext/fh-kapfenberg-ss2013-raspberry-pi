# coding: utf-8
from libthermalraspi.services.sampleCollector import SampleCollector
from libthermalraspi.database.DataStoreSQL import DataStoreSQL

import datetime
import time
import os

class ParallelSampleCollector(SampleCollector):
    __sensorList = []
    __runState = 0
        
    def __init__(self):
        #Nothing to do here
        pass
 
    def configuration(self, sensorList=[] ):
        """Sammler der Messdaten mit Liste aller abzufragenden
        Sensoren versorgen.
        
        @param sensorList Liste von Sensor-Instanzen
        """
        self.__sensorList.extend(sensorList)
        pass
    
    def run(self, timeDelta):
        """Messungen starten und Zeitintervall zwischen zwei Abfragen
        der Sensormesswerte in Millisekunden festlegen. Messungen erfolgen, bis stop()
        aufgerufen wird.
        
        @param timeDelta Intervall in Millisekunden zwischen zwei Messungen
        """
        self.__runState = 1

        while (self.__runState == 1):
            self.__getAllSensorTemperatures()
            # Umrechnung timeDelta Mikrosekunden-int-Wert zu Millisekunden f�r die sleep
            # Bsp.: timedelta = 5 => /1000 => 0,005  ==> interpretiert als Sekunden in sleep
            sleepTimeInSeconds = datetime.timedelta(0,0,timeDelta).microseconds/1000.0
            time.sleep(sleepTimeInSeconds)  # Argument ist Wert in Sekunden(-bruchteilen)
        pass
    
    def stop(self):
        """Messwerterfassung stoppen."""
        self.__runState = 0
        pass
        
    def getRunstate(self):
        return self.__runState
        pass
    
    def __getAllSensorTemperatures(self):
        imTheFather = True
        children = {}   #dictionary sensor:childPid
        errorCode = 0
        pipein, pipeout = os.pipe()
      
        for sensor in self.__sensorList:
            child = os.fork()
            if child:
                children[sensor] = child
            else:
                imTheFather = False
                os.close(pipein)

                os.write(pipeout, str(sensor.get_temperature() ) + "\n" )
                
                os.close(pipeout)
                os._exit(0)
         
        if imTheFather:
            _sensorTemp = os.fdopen(pipein)
            for sensor, childPid in children.items():
                os.waitpid(childPid, 0)
                _sensorName = type(sensor).__name__
                
                'Persistiere Messdaten in DB'
                DataStoreSQL.add_sample(datetime.datetime.now(), _sensorName, _sensorTemp.readline(), errorCode)
                
        pass
