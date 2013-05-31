#!/usr/bin/python

from libthermalraspi.database.DataStoreSQL import DataStoreSQL
from libthermalraspi.services.SensorConfigReader import SensorConfigReader
from libthermalraspi.services.parallelSampleCollector import ParallelSampleCollector
from libthermalraspi.programlooper import ProgramLooper

import sqlite3

# parameters: to be parsed from the commandline using argparse
DBFILE = "/tmp/some.db"
INTERVAL = 3.14159265359 # seconds
SENSORS = "/tmp/sensors.cfg"

db = sqlite3.connect(DBFILE)
store = DataStoreSQL(db)

sensors = SensorConfigReader(SENSORS).read()
collector = ParallelSampleCollector( store=store, sensorList=sensors )

# this is the ominous looping construct that needs to be done:
looper = ProgramLooper(INTERVAL)

collector.run(looper)
# collector.run([1,2,3])
