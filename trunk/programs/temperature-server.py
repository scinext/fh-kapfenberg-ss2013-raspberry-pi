#!/usr/bin/python

from optparse import OptionParser
from libthermalraspi.database.DataStoreInMemory import DataStoreInMemory
from libthermalraspi.network.tempserver import TempServer
import sqlite3
import logging

# instantiate TempServer as see fit, and run it
parser = OptionParser()
parser.add_option("-f", "--dbfile", 
                  action="store", type="string", dest="DBFILE", default="/tmp/some.db", help="used sqlite file name (default=/tmp/some.db)")
parser.add_option("-l", "--logfile", 
                  action="store", type="string", dest="LOGFILE", default="", help="used logfile (default=/tmp/tempserver.log)")
parser.add_option("-p", "--port",
                  action="store", type="int", dest="PORT", default=2345, help="used port (default=2345)")
parser.add_option("-d", "--dummy",
                  action="store_true", dest="DUMMY", default=False, help="dummy usage, no dbfile required (default=False)")
parser.add_option("-H", "--host",
                  action="store", dest="HOST", default="localhost", help="hostname (default=localhost)")

(options, args) = parser.parse_args()

print("Config: dummy=%s, dbfile=%s, port=%s" % (options.DUMMY, options.DBFILE, options.PORT))

if options.DUMMY:
    store = DataStoreInMemory()
    store.initSomeTestData()
else:
    db=sqlite3.connect(options.DBFILE)
    store=DataStoreSQL(db)

if options.LOGFILE=="":
    options.LOGFILE=None

#addSignalHandler()
#TOTO Signalhandler 
tempServer = TempServer(host=options.HOST, port=options.PORT, datastore=store, logfile=options.LOGFILE, loglevel=logging.INFO)
tempServer.start()



