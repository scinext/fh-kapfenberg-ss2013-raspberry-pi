#!/usr/bin/python

# parameters: to be parsed from the commandline using argparse
DBFILE = "/tmp/some.db"
INTERVAL = 3.14159265359 # seconds
SENSORS = "/etc/sensor.cfg"


db = sqlite3.connect(DBFILE)
store = DataStoreSQLite(db)
sensors = eval(file(SENSORS).read(), { 'LM73': LM73Device, })
collector = ParallelSampleCollector(
    store=store,
    sensors=sensors)

# this is the ominous looping construct that needs to be done:
looper = SleepingLooperWithSignalHandling(INTERVAL)

collector.run(looper)
