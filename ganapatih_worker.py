import gearman
import pymongo
from datetime import datetime
import json
import sys

c = pymongo.Connection()
db = c["ganapatih"]

gm_worker = gearman.GearmanWorker(["127.0.0.1"])

def insert_dbase(gearman_worker, gearman_job):
    sys.stdout.write('inserting dbase at '
                     + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
                     + '\n')
    db.panics.insert(json.loads(gearman_job.data))
    sys.stdout.write('inserting success at '
                     + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
                     + '\n')
    return json.dumps(gearman_job.data)

gm_worker.set_client_id('insert_dbase_worker')
gm_worker.register_task('register', insert_dbase)
gm_worker.work()
