# worker.py

import os

from redis import Redis
from rq import Worker, Queue, Connection

from diannQ_job import process_job


listen = ['default']

conn = Redis(host='192.168.1.176', port='6379')

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
