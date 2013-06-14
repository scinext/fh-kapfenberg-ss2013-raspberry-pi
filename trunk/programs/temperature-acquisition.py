#!/usr/bin/python

from libthermalraspi.database.DataStoreInMemory import DataStoreInMemory
from libthermalraspi.services.SensorConfigReader import SensorConfigReader
from libthermalraspi.services.parallelSampleCollector import ParallelSampleCollector
from libthermalraspi.programlooper import ProgramLooper
from libthermalraspi.database.DataStoreSQL import DataStoreSQL

from optparse import OptionParser
import sqlite3

parser = OptionParser()
parser.add_option("-f", "--dbfile", 
                  action="store", type="string", dest="DBFILE",
                  default="/tmp/some.db",
                  help="used sqlite file name (default=/tmp/some.db)")
parser.add_option("-s", "--sensors", 
                  action="store", type="string", dest="SENSORS",
                  default="/tmp/sensors.cfg",
                  help="sensor config file path (default=/tmp/sensors.cfg)")
parser.add_option("-i", "--interval",
                  action="store", type="float", dest="INTERVAL",
                  default=3,
                  help="used interval in seconds(default=3)")
parser.add_option("-d", "--dummy",
                  action="store_true", dest="DUMMY",
                  default=False,
                  help="dummy usage (default=False)")

(options, args) = parser.parse_args()

print("Config: dummy=%s, dbfile=%s, interval=%s, sensorconfig=%s" % \
      (options.DUMMY, options.DBFILE, options.INTERVAL, options.SENSORS))

if options.DUMMY:
    store = DataStoreInMemory()
    store.initSomeTestData()
else:
    db=sqlite3.connect(options.DBFILE)
    store=DataStoreSQL(db)

sensors = SensorConfigReader(options.SENSORS).read()
collector = ParallelSampleCollector( store=store, sensorList=sensors )

# this is the ominous looping construct that needs to be done:
looper = ProgramLooper(options.INTERVAL)

collector.run(looper)
