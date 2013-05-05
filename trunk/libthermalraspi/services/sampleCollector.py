from libthermalraspi.services.dataStore import DataStore

import datetime
import time
import os

class SampleCollector():
    __sensorNames = []
    __runState = 0
        
    def __init__(self):
        #Nothing to do here
        pass
 
    def configuration(self, sensorNamesList=[] ):
        """Sammler der Messdaten mit Liste aller abzufragenden Sensoren versorgen."""
        self.__sensors.extend(sensorNamesList)
        pass
    
    def run(self, timeDelta):
        """Messungen starten und Zeitintervall zwischen zwei Abfragen
        der Sensormesswerte in Millisekunden festlegen. Messungen erfolgen, bis stop()
        aufgerufen wird."""
        self.__runState = 1

        while (self.__runState == 1):
            self.__getAllSensorTemperatures()
            # Umrechnung timeDelta Mikrosekunden-int-Wert zu Millisekunden für die sleep
            # Bsp.: timedelta = 5 => /1000 => 0,005  ==> interpretiert als Sekunden in sleep
            sleepTimeInSeconds = datetime.timedelta(0,0,timeDelta).microseconds/1000.0
            time.sleep(sleepTimeInSeconds)  # Argument ist Wert in Sekunden(-bruchteilen)

        pass
    
    def stop(self):
        """Messwerterfassung stoppen."""
        self.__runState = 0
        pass
        
    def __getAllSensorTemperatures(self):
        imTheFather = True
        children = {}   #dictionary sensorname:childpid
        errorCode = 0
        pipein, pipeout = os.pipe()
        
        for sensor in self.__sensorNames:
            child = os.fork()
            if child:
                children[sensor] = child
            else:
                imTheFather = False
                os.close(pipein)
                os.write(pipeout, {str(sensor) : float(getattr(sensor, 'get_temperature')) })
                os.close(pipeout)
                os._exit(0)
        
        if imTheFather:
            readSensorTemp = os.fdopen(pipein)     #dictionary sensorname:sensorTemperatur
            for childkey, childvalue in children.items():
                os.waitpid(childvalue, 0)
                DataStore.add_sample(datetime.datetime.now(), childkey, readSensorTemp, errorCode)




