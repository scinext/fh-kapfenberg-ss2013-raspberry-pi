#!/usr/bin/python

import threading
import time
import os

# items are produced by one thread, and consumed by another.
# items are big, and stored in a database, indexed by their ID.
database = {}

# the IDs (simple integer values) are enqueued by the producer, and
# dequeued by a consumer who then looks up the corresponding item in
# the database.
queue = []

producer_interval = 1
consumer_interval = 1

class Producer(threading.Thread):
    def run(self):
        item_no = 0
        while True:
            queue.append(item_no)
            database[item_no] = 'some big chunk to process in another thread'
            item_no += 1
            time.sleep(producer_interval)

class Consumer(threading.Thread):
    def run(self):
        while True:
            if len(queue) == 0:
                time.sleep(consumer_interval)
                continue

            # dequeue and get next item ID
            item_no = queue[0]
            del queue[0]

            # get and remove item to process
            item = database[item_no]
            del database[item_no]

            # print("processing '%s'" % item)

if __name__ == '__main__':
    print os.getpid()
    consumer = Consumer()
    producer = Producer()

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()

