# Thermal Sensors #

A thermal sensor is something that gives the temperature in degrees Celsius, a floating point number. Pythonically, it is something that supports the method `get_temperature()`, returning a floating point number.

There are several implementations.

  * **I2C Temperature Sensor**: [Microchip TC74](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010749)
  * **I2C Temperature Sensor**: [Analog Devices AD7414](http://www.analog.com/en/mems-sensors/digital-temperature-sensors/ad7414/products/product.html)
  * **I2C Humidity and Temperature Sensor HYT221**
    * [Data sheet](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempHumiSensor-HYT221-Datenblatt_DE.pdf)
    * [Protocol description](http://fh-kapfenberg-ss2013-raspberry-pi.googlecode.com/svn/trunk/docs/TempHumiSensor-HYT221-Protokollbeschreibung_DE.pdf)
    * [Source code](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/sensors/hyt221.py) (using `read/write`)
    * [Source code](http://code.google.com/p/fh-kapfenberg-ss2013-raspberry-pi/source/browse/trunk/libthermalraspi/sensors/hyt221_smbus.py) (using `python-smbus` package)
  * (Possibly a couple other pieces of real hardware)
  * **TCP Proxy Sensor**. Imagine that the sensors are spread across a, say, food warehouse. I2C imposes a maximum cable length of only a few meters, so we want to use TCP to connect a local sensor object to a remote sensor. [Proxy pattern](http://en.wikipedia.org/wiki/Proxy_pattern), applied.
  * **UNIX Domain Proxy Sensor**. Same as TCP, but using [UNIX Domain](http://en.wikipedia.org/wiki/Unix_domain_socket) stream sockets instead. Unix Domain sockets are used to connect processes inside the same machine, so its main purpose won't be to bridge long distances. However, it can be used to decouple real sensors from their users, by moving them out into separate processes.
  * **Composite sensor**. Determines the average temperature based on a number of real sensors.
  * **Composite parallel sensor**. Like composite sensor, determines the average temperature based on a number of real sensors. On each call to `get_temperature()`, it uses the `fork(2)` system call to create one process for each of the child sensors, and `wait(2)` and `exit(3)` to coordinate their lifetimes. Each child process communicates the temperature to the parent using a `pipe(2)` which it inherited from the parent. It so determines the child temperatures in parallel, rather than one after the other. This can greatly reduces response time, especially if proxy sensors are configured.
  * **Random sensor**. For testing and simulation. Uses `/dev/random` to retrieve 64 bit random numbers from the system's entropy pool, which are then converted to temperatures in a certain configurable range.