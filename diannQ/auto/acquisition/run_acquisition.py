import redis
from rq import Queue
import sys
from pathlib import Path
import shutil

from diannQ.diannQ_job import process_auto_job


def get_server_path(name):
    server_locations = {
        "G": "G:/RAW/",
        "M": "M:/RAW/",
        "O": "O:/RAW_ttp/",
        "F": "F:/RAW/",
        "I": "I:/RAW/",
        "V": "V:/RAW/"
    }

    return Path(server_locations[name[0]])


# get all flags
args = sys.argv[1:]

raw_data_path = Path(args[0])
fasta_type = "homo_sapiens"
if len(args) > 1:
    fasta_type = args[1]


# copy data from aquisition pc to server
raw_data_name = raw_data_path.name
server_path = get_server_path(raw_data_name) / raw_data_name
shutil.copytree(raw_data_path, server_path)


conn = redis.Redis(host="192.168.1.176", port=6379)
q = Queue(connection=conn)
q.enqueue(process_auto_job, raw_data_name, fasta_type, job_timeout=99999)
