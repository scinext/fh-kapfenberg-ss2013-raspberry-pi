#!/usr/bin/python

from libthermalraspi.services.parallelSampleCollector import ParallelSampleCollector
from libthermalraspi.services.dataStoreStdOut import DataStoreStdOut
from libthermalraspi.sensors.simulation import CyclicThermometer

store = DataStoreStdOut()

collector = ParallelSampleCollector()
collector.configuration(sensorList=(CyclicThermometer((1, 2, 3)), 
                                    CyclicThermometer((4, 5, 6))),

                        # wish I could pass the store in, rather than
                        # having to use a checked-in database
                        # store=store
    )

collector.run(1000)
