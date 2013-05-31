#!/usr/bin/python
from optparse import OptionParser
from libthermalraspi.database import DataStoreInMemory
import sqlite3
# parameters: to be parsed from the commandline using argparse
#DUMMY = False
#DBFILE = "/tmp/some.db" # used if not DUMMY
#PORT = 2345

#db = sqlite3.connect(DBFILE)
#store = DataStoreSQLite(db)

# instantiate TempServer as see fit, and run it
parser = OptionParser()
parser.add_option("-f", "--dbfile", 
                  action="store", type="string", dest="DBFILE", default="/tmp/some.db", help="used sqlite file name (default=/tmp/some.db)")
parser.add_option("-p", "--port",
                  action="store", type="int", dest="PORT", default=2345, help="used port (default=2345)")
parser.add_option("-d", "--dummy",
                  action="store_true", dest="DUMMY", default=False, help="dummy usage (default=False)")

(options, args) = parser.parse_args()

print("Config: dummy=%s, dbfile=%s, port=%s" % (options.DUMMY, options.DBFILE, options.PORT))

if options.DUMMY:
    store = DataStoreInMemory()
else:
    db=sqlite3.connect(options.DBFILE)
    store=DataStoreSQL(db)

