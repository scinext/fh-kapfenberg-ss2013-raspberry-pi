#!/usr/bin/python

import time

class SleepingLooper:
    def __init__(self, interval_seconds):
        self.__interval = interval_seconds
        self.__counter = 0

        # to be set from signal handler
        self.__stop = False
        
    def __iter__(self):
        while not self.__stop:
            yield self.__counter
            self.__counter += 1
            time.sleep(self.__interval)

looper = SleepingLooper(1.5)
for i in looper:
    print i
