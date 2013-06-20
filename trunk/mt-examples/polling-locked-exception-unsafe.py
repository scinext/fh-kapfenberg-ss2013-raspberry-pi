#!/usr/bin/python

import threading
import time
import os

# --------------------------------------------------------------------
# WARNING: THIS PROGRAM IS A DEMONSTRATION OF SOME OF THE REALLY BAD
# (BUT, SADLY, POPULAR) PRACTICES OF INTER-THREAD COMMUNICATION. DON'T
# EVER COPY FROM IT!!!

# WEAKNESSES:

# * locking is in place, but not exception-safe. lock remains held if
#   the critical section is terminated by an exception
# * the consumer polls for data. there sure is a better way.
# * the producer produces no matter what. if the consumer does not
#   consume fast enough, the program will run out of memory.
# --------------------------------------------------------------------


# items are produced by one thread, and consumed by another.
# items are big, and stored in a database, indexed by their ID. (using
# a dictionary as a symbolic database.)
database = {}

# the IDs (simple integer values) are enqueued by the producer, and
# dequeued by a consumer who then looks up the corresponding item in
# the database.
queue = []

lock = threading.Lock()

producer_interval = 1
consumer_interval = 1

class Producer(threading.Thread):
    def run(self):
        item_no = 0
        while True:
            # begin critical section
            lock.acquire()
            queue.append(item_no)
            database[item_no] = 'some big chunk to process in another thread'
            item_no += 1
            lock.release()
            # end critical section

            time.sleep(producer_interval)

class Consumer(threading.Thread):
    def run(self):
        while True:
            # begin critical section
            lock.acquire()

            if len(queue) == 0:
                # end critical section (nothing to do)
                lock.release()

                time.sleep(consumer_interval)
                continue

            # dequeue and get next item ID
            item_no = queue[0]
            del queue[0]

            # get and remove item to process
            item = database[item_no]
            del database[item_no]

            # print("processing '%s'" % item)

            # end critical section
            lock.release()
            

if __name__ == '__main__':
    print os.getpid()
    consumer = Consumer()
    producer = Producer()

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()

