#!/bin/python

import os

from libthermalraspi.sensors.hypothetical import HypotheticalThermometer

a = dict()
pipes = dict()

my_list = []

test1 = HypotheticalThermometer(2,12)
test2 = HypotheticalThermometer(4,10)
test3 = HypotheticalThermometer(6,8)

my_list.append(test1)
my_list.append(test2)
my_list.append(test3)

# loop over all elements
for index, item in enumerate(my_list):
    # PIPE
    # you write in on the one side and read on the other side
    # pipein  < === > pipeout
    parentRead, childWrite = os.pipe()
    # fork a child process
    child = os.fork()
    
    # os.fork(): Return 0 to child process and PID of child to parent process.
    if (child == 0):
        # write some formatted temp stuff in the pipe
        os.write(childWrite, str(my_list[index].get_temperature()).zfill(7))
        exit()
    else:
        # save the pid of all childs
        a[index]=child
        pipes[index]=parentRead
        # close not used filedescriptor
        os.close(childWrite)

# just a loop for the element-count
for k in a:
    # wait for any child to return
    pid, status = os.wait()
    # find child-pid in the dictionary to save corresponding temp
    for k2,v in a.items():
        if (v == pid):
            # read exact 7 bytes from pipe
            a[k2] = os.read(pipes[k2],7)
            print("%s with pid(%s) sent: %3.3f" % (k2,v,float(a[k2])))

if __name__ == '__main__':
    pass
