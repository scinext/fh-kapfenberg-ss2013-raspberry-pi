# Linux on the Raspberry Pi #

To get Linux running on the Raspi, and to configure it in a way that
it serves its purpose of a development machine for our project, you'll
need to perform a couple of steps. These are going to be outlined here
briefly.

# Initial Board Setup #

[Here's](http://www.raspberrypi.org/wp-content/uploads/2012/12/quick-start-guide-v1.1.pdf) a great quick start guide to bring a Linux OS image onto the
Pi.

If you have Linux on your PC, you'll find the
[Win32DiskImager](http://sourceforge.net/projects/win32diskimager/)
section hard to follow. Skip it, and simply instead

```
# cat 2013-02-09-wheezy-raspbian.img > /dev/sdc
```

where `/dev/sdc` is your SD card. (Your situation may be
different; check `/proc/partitions` for yours.) Make sure you
unmount it before if it got automounted (likely by your desktop).

## Configuration ##

The `raspi-config` tool is used to perform initial
configuration. You'll see it at first boot, and can call it anytime
afterwards if need be.

It is a good idea to carry out the following functions,

  * _Expand root partition to fill SD card_ (effective after next reboot)
  * _Enable or disable ssh server_. You'll want to enable SSH access if you want to login from you laptop. Windows users use [PuTTY](http://www.putty.org/) for remote login.



Ah yes, I2C: it is probably a good idea to have the necessary kernel
modules loaded at startup. Add these to `/etc/modules`:

```
i2c-bcm2708
i2c-dev
```

# Packages #

The _raspbian_ image is a [Debian](http://www.debian.org/)
derivative. As such, it uses
[APT](https://help.ubuntu.com/community/AptGet/Howto) for package
management. Install the packages needed for our project like follows,

```
# apt-get install \
   subversion \
   i2c-tools
```

When done, add yourself to the `i2c` group to have access to the
I2C bus `/dev/i2c-1`. As user `root` (or using `sudo`),

```
# usermod -a -G i2c pi
```

(List to be expanded.)