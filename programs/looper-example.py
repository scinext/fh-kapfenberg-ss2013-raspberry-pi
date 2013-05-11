#!/usr/bin/python

import time

class SleepingLooper:
    def __init__(self, interval_seconds):
        self.__interval = interval_seconds
        self.__counter = 0
        
    def __iter__(self):
        while True:
            yield self.__counter
            self.__counter += 1
            time.sleep(self.__interval)


looper = SleepingLooper(1.5)
for i in looper:
    print i
