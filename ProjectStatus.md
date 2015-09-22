

# Sensors #

**Todo**

| Stefan Winkler, Martin Steinbauer | Fix LM73 `set_resolution()` |
|:----------------------------------|:----------------------------|
| ???                               | LM73: `get_temperature()` does not respect resolution from Control/Status register |

  * **[LM73](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempSensor-LM73.pdf)**. We have an implementation (by Helmut Kopf and Patrick Gröller) that can
    * Convert the temperature register based on the precision configuration from the "control/status" register
    * Configure the precision (set the "control/status" register)
  * **[TC74](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempSensor-TC74.pdf)**. Done (to be verified).
  * **[AD7414](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempSensor-AD741x.pdf)**. Done (to be verified).
  * **[HYT221](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempHumiSensor-HYT221-Protokollbeschreibung_DE.pdf)**. Done (to be verified).

# Temperature Sample Database #

Done (the reader side still to be verified).

We have an [interface](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/database/DataStore.py),
and both [an in-memory](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/database/DataStoreInMemory.py)
and [a SQL](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/database/DataStoreSQL.py) implementation. The latter uses [Python's DBAPI2](http://www.python.org/dev/peps/pep-0249/) which decouples it from any concrete database. In the project, SQLite3 is used as a database.

# Sample Acquisition #

**Todo**

| Martin Krainer, Markus Koller | Write unit tests for ParallelSampleCollector, using DataStoreInMemory |
|:------------------------------|:----------------------------------------------------------------------|

A [parallelized (using multiple processes) temperature sample acquisition](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/services/parallelSampleCollector.py) is in place.

A main program does database and sensors setup, and then drives the
main loop of the acquisition. A [Python generator is used to control the loop](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/programlooper.py) and, most important, its termination using a signal handler.

A couple of unit tests are still to be written to test several aspects such as

  * Regular operation of a couple of sensors
  * Error scenarios:
    * IOError on a sensor (can be simulated; write a dedicated sensor that always throws)
    * what else?

# Temperature Sample Server #

**Todo**

| Patrick Gröller | Restructure XML protocol part and server to let one _assemble_ the software (see below) |
|:----------------|:----------------------------------------------------------------------------------------|
| Helmut Kopf     | Review the callback mechanism where threads are (un)registered (locking issues)         |
| Florian Dulzky, Markus Neubauer | Real-life final _program_                                                               |

**The network part** is basically done. The [code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/network/tempserver.py server class] is parallel and handles each command in a dedicated thread. There are still some locking issues that need to be resolved.

**The protocol part** needs rework. Should use the `DataStore`
interface to collect data. Currently, it uses a hardcoded list of
return samples; this will be done using a `DataStoreInMemory` ---
which is passed in from the main program in the "dummy" mode (very much like the [acquisition program](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/programs/temperature-acquisition.py)). The real-life `DataStoreSQL` will also be passwd in by the main program.

**The real-life final program** will

  * Fullfill requests from a database (presumably from the same database that is filled by the acquisition program)
  * Provide a "dummy" option for easy operation, for use by the Android client developer(s).
  * Use the `argparse` module to interpret commandline parameters

Use [this](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/programs/temperature-server.py) as a starting point.

# Android App #

**Todo**

| Ludwig Lindlbauer | ? |
|:------------------|:--|