import redis
from rq import Queue
import sys
from diannQ.diannQ_job import process_user_job


# get all flags
args = sys.argv[1:]

if args[1] == "":
    args[1] = "--lib  --threads 32 --verbose 3 --out output/report.tsv --qvalue 0.01 --matrices --out-lib output/report-lib.tsv --gen-spec-lib --predictor --min-fr-mz 200 --max-fr-mz 1800 --met-excision --cut K*,R* --missed-cleavages 1 --min-pep-len 7 --max-pep-len 30 --min-pr-mz 300 --max-pr-mz 1800 --min-pr-charge 1 --max-pr-charge 4 --unimod4 --reanalyse --relaxed-prot-inf --pg-level 2 --species-genes"


arg_str = " ".join(str(element) for element in args)
args = arg_str.split()
args.insert(0, "--f")


conn = redis.Redis(host="192.168.1.176", port=6379)
q = Queue(connection=conn)
q.enqueue(process_user_job, args)