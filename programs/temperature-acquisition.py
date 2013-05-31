#!/usr/bin/python
from optparse import OptionParser
from libthermalraspi.database import DataStoreInMemory
from libthermalraspi.services.SensorConfigReader import SensorConfigReader
from libthermalraspi.services.parallelSampleCollector import ParallelSampleCollector
from libthermalraspi.programlooper import ProgramLooper
from libthermalraspi.database.DataStoreSQL import DataStoreSQL

import sqlite3

# parameters: to be parsed from the commandline using argparse
#DUMMY = False
#DBFILE = "/tmp/some.db" # used if not DUMMY
#PORT = 2345
#SENSORS = "/tmp/sensors.cfg"
#db = sqlite3.connect(DBFILE)
#store = DataStoreSQLite(db)

# instantiate TempServer as see fit, and run it
parser = OptionParser()
parser.add_option("-f", "--dbfile", 
                  action="store", type="string", dest="DBFILE", default="/tmp/some.db", help="used sqlite file name (default=/tmp/some.db)")
parser.add_option("-s", "--sensors", 
                  action="store", type="string", dest="SENSORS", default="/tmp/sensors.cfg", help="sensor config file path (default=/tmp/sensors.cfg)")
parser.add_option("-p", "--port",
                  action="store", type="int", dest="PORT", default=2345, help="used port (default=2345)")
parser.add_option("-i", "--interval",
                  action="store", type="int", dest="INTERVAL", default=3, help="used interval in seconds(default=3)")
parser.add_option("-d", "--dummy",
                  action="store_true", dest="DUMMY", default=False, help="dummy usage (default=False)")

(options, args) = parser.parse_args()

print("Config: dummy=%s, dbfile=%s, port=%s, interval=%s, sensorconfig=%s" % (options.DUMMY, options.DBFILE, options.PORT, options.INTERVAL, options.SENSORS))

if options.DUMMY:
    store = DataStoreInMemory()
else:
    db=sqlite3.connect(options.DBFILE)
    store=DataStoreSQL(db)

sensors = SensorConfigReader(options.SENSORS).read()
collector = ParallelSampleCollector( store=store, sensorList=sensors )

# this is the ominous looping construct that needs to be done:
looper = ProgramLooper(options.INTERVAL)

collector.run(looper)
# collector.run([1,2,3])
    

