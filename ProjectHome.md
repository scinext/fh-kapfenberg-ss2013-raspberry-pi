# Systems Programming on Linux #

This project is a companion of a course on systems programming at the [Fachhochschule Joanneum](http://www.fh-joanneum.at) in Kapfenberg, Austria. Using [Python](http://www.python.org) and the great [Raspberry Pi](http://www.raspberrypi.org/) hardware, we explore the nature of the Linux operating system.

Here's the design document, err, a scribble of ideas collected during the first course unit. It is sort of UML, roughly describing the project's goal.

  * The center hierarchy represents the core of the project - [thermal sensors of various kinds](ThermalSensorHierarchy.md).
  * On the right you see an application of the _proxy_ pattern which gives us the opportunity to play with network sockets.
  * On the left there are some applications - a [WSGI web frontend, an Android App, and a data logger](Applications.md).
  * What you don't see is
    * The [project status page](ProjectStatus.md).
    * The Raspberry and Linux. [Read more](OverviewInstructions.md) for instructions, tutorials, links.
    * The [I2C Bus](I2CBus.md) which hosts the sensors that we use
    * The ["theoretical" explanations](TheoreticalExplnations.md) thrown in between the hacking sessions

![https://lh6.googleusercontent.com/-1pkSJlTQHEc/UU7iKhXutCI/AAAAAAAAA78/A1GDh0oAjmc/s591/IMG_20130315_221445.jpg](https://lh6.googleusercontent.com/-1pkSJlTQHEc/UU7iKhXutCI/AAAAAAAAA78/A1GDh0oAjmc/s591/IMG_20130315_221445.jpg)