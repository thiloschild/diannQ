import redis
from rq import Queue
import sys
from diannQ.diannQ_job import process_auto_job
import pyrsync




# get all flags
args = sys.argv[1:]

raw_data_path = args[0]
fasta_type = "human"
if len(args) > 1:
    fasta_type = args[1]


# copy data from aquisition pc to server
raw_data_server_path = ...
raw_data = ...

conn = redis.Redis(host="192.168.1.176", port=6379)
q = Queue(connection=conn)
q.enqueue(process_auto_job, raw_data, fasta_type)
