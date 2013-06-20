#!/usr/bin/python

from Queue import Queue
import threading
import time
import os

# --------------------------------------------------------------------
# FROM THIS ONE YOU CAN COPY. THREAD SAFE, NON-POLLING!
# --------------------------------------------------------------------

# items are produced by one thread, and consumed by another.
# items are big, and stored in a database, indexed by their ID. (using
# a dictionary as a symbolic database.)
database = {}

item_no = 0

# the IDs (simple integer values) are enqueued by the producer, and
# dequeued by a consumer who then looks up the corresponding item in
# the database. the queue has a maximum size to throttle the producer
# in case consuming is delayed.
queue_size = 10
queue = Queue(10)

# the lock protects only the database. unlike the other, polling,
# versions, the queue protects itself.
lock = threading.Lock()

class Producer(threading.Thread):
    def run(self):
        global item_no
        while True:
            with lock:
                database[item_no] = 'some big chunk to process in another thread'
                item_no += 1
            # announce item. blocks if queue is full.
            print 'producing %d ...' % (item_no-1)
            queue.put(item_no-1)

class Consumer(threading.Thread):
    def run(self):
        while True:
            # get next item. blocks if queue is empty.
            next_item_no = queue.get()
            with lock:
                # get and remove item to process
                item = database[next_item_no]
                del database[next_item_no]

                print("processing '%s'" % item)

if __name__ == '__main__':
    print os.getpid()
    consumers = []
    for i in xrange(2):
        consumer = Consumer()
        consumer.start()
        consumers.append(consumer)
    producers = []
    for i in xrange(2):
        producer = Producer()
        producer.start()
        producers.append(producer)

    for consumer in consumers:
        consumer.join()
    for producer in producers:
        producer.join()

