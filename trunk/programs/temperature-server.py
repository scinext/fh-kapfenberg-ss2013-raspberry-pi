#!/usr/bin/python

# parameters: to be parsed from the commandline using argparse
DUMMY = False
DBFILE = "/tmp/some.db" # used if not DUMMY
PORT = 2345

db = sqlite3.connect(DBFILE)
store = DataStoreSQLite(db)

# instantiate TempServer as see fit, and run it
