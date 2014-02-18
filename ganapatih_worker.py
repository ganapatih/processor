import gearman
import pymongo
from datetime import datetime
import json
import sys

c = pymongo.Connection()
db = c["ganapatih"]

gm_worker = gearman.GearmanWorker(["127.0.0.1"])

def register_insert(gearman_worker, gearman_job):
    t = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
    sys.stdout.write('[%s] :: Registering new user\n' % t)
    db.register.insert(json.loads(gearman_job.data))
    sys.stdout.write('[%s] :: User registered\n' % t)
    return json.dumps(gearman_job.data)

def korban_insert(gearman_worker, gearman_job):
    t = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
    sys.stdout.write('[%s] :: Inserting korban data\n' % t)
    db.korban.insert(json.loads(gearman_job.data))
    sys.stdout.write('[%s] :: Korban data inserted\n' % t)
    return json.dumps(gearman_job.data)

def relawan_insert(gearman_worker, gearman_job):
    t = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
    sys.stdout.write('[%s] :: Inserting relawan data\n' % t)
    db.relawan.insert(json.loads(gearman_job.data))
    sys.stdout.write('[%s] :: Relawan data inserted\n' % t)
    return json.dumps(gearman_job.data)

gm_worker.set_client_id('register_new_user')
gm_worker.register_task('register', register_insert)
gm_worker.set_client_id('insert_korban')
gm_worker.register_task('korban', korban_insert)
gm_worker.set_client_id('insert_relawan')
gm_worker.register_task('relawan', relawan_insert)
gm_worker.work()
