# Applications using the Sensor Hierarchy #

The primary application is a data logger --- a process that
periodicaly scans a configured set of sensors, and logs their reports
into a database.

(As this is the only application so far, we document it here. To be
moved out if need be.)

## Data Logger ##

See
[here](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/docs/Datalogger-UML.png)
for a UML diagram.

### The DataStore Interface and its Responsibilities ###

We use a "DataStore" class to abstract away databases. Nobody wants
to carry the burden of a database when, for example, hacking on a
visualization GUI.

A data store's job is to

  * store samples
  * retrieve samples

The store is filled by somebody who produces samples at a regular
interval. Pythonically, a sample is simply a tuple
`(timestamp, sensorname, temperature, status)`.
One can imagine that the following code fragment would produce one sample.

```
import datetime

try:
    temperature = t.get_temperature()
    status = 0
except Thermometer.Error as e:
    temperature = 0.0
    status = e.status

sample = (datetime.datetime.utcnow(), 
          "Sensor in the third row, middle, bottom",
	  temperature,
          status)
store.add_sample(sample)
```

Samples are retrieved based on a range like so,

```
samples = store.get_samples(from, to)
```

where `from` and `to` are `datetime.datetime` objects. If
either end is unspecified, it is passed as `None`. Note that the
store may choose to raise an exception if the number of samples in the
specified range is too high. In this case, the user has to split the
desired range into multiple smaller ranges and retrieve those one by
one.

### SQLite3 DataStore Incarnation ###

The "real life" incarnation of a data store maintains a SQLite3
database. The database has a single table "samples" which is set up to
contain the sample tuples.

```
create table samples (
  timestamp datetime,
  sensorname varchar(30),
  temperature real,
  status int
)
```

A single process is dedicated to filling the database. Note that
SQLite3 supports access to a database from multiple processes, but
only one of those can write to it. (See
[here](http://www.sqlite.org/faq.html#q5) for the whole story.)

This retriction is fine for us --- we can have multiple readers, which
is what we will.

### In-Memory DataStore Incarnation ###

For testing (we want to implement a TCP server that serves samples),
there has to be one implementation of the `!DataStore` interface
which keeps its samples in memory. One possibility of doing this is to
keep a list of tuples (the samples), append to it in
`store.add_sample(s)`, and sort the list by its timestamp. Like
so,

```
def add_sample(sample):
    self.__samples.append(sample)
    self.__samples = sorted(self.__samples, lambda a,b: a[0]<b[0])
```

This not the most efficient way of maintaining an ordered list, but
anyway, it's not for sale.

### The Data Logger Server and the Protocol ###

A simple TCP server answers queries from clients, by making the
collected samples visible to the outside world. The server's design is
_iterative_, as follows.

  * **It handles one incoming connection after the other**. No threads are created, no process is forked.
  * **It handles one request per connection**. The server sits in a call to `accept()` until a connection comes in, then reads the request until complete, and then writes the response. The connection is closed after the response has been written.

The protocol spoken between a client and the server is XML
based. Currently we have only one possible request,
`get_samples(from, to)`, but we can imagine that there may be more
as the demand for the application grows. Hence any request must carry
its identifier with it (which is good protocol design anyway).

**Request**:

```
<request id="get_samples" from="2013-01-30 00:00:00" to="2013-01-30 23:59:59" />
```

In Python, you use the following to convert back and forth between
`datetime.datetime` and strings,

```
s = "%04d-%02d-%02d %02d:%02d:%02d" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
dt = datetime.datetime.strptime(s, '%d-%m-%Y %H:%M:%S')
```

**Response**:

```
<response>
  <status error="ok" />
  <samples>
    <sample timestamp="2013-04-30 08:03:38"
            sensorname="Sensor in the third row, middle, bottom"
	    temperature="10.25"
	    status="0" />
    <sample timestamp="2013-04-30 08:03:38"
            sensorname="Sensor in the third row, middle, top"
	    temperature="11.5"
 	    status="0" />
  </samples>
</response>
```

Note that we have two `status` attributes in the response. The
response global `status` is the status of the entire response, and
this can be `ok`, `overflow` (if the server encountered a
query result overflow condition for example), and whatnot. The
per-sample `status` attribute is the error status of one
particular sensor.