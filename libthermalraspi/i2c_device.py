import os
import fcntl

class I2CDevice(object):
    I2C_SLAVE = 0x0703 # from <linux/i2c-dev.h>
    def __init__(self, busno, addr):
        fd = os.open('/dev/i2c-%d' % busno, os.O_RDWR)
        fcntl.ioctl(fd, self.I2C_SLAVE, addr)
        self.__fd = fd
        pass
    def write(self, msg):
        os.write(self.__fd, msg)
        pass
    def read(self, n):
        msg = os.read(self.__fd, n)
        assert len(msg) == n
        return msg
    pass

