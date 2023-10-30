import redis
from rq import Queue
import sys
from diannQ.diannQ_job import process_user_job


# get all flags
args = sys.argv[1:]

conn = redis.Redis(host="192.168.1.176", port=6379)
q = Queue(connection=conn)
q.enqueue(process_user_job, args)
