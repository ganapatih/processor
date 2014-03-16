import gearman
import pymongo
from datetime import datetime
import json
import sys
from dateutil.parser import parse
from time import sleep

# create mongo connection
c = pymongo.Connection()
db = c["ganapatih"]
# define worker
gm_worker = gearman.GearmanWorker(["127.0.0.1"])
t = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")


def register_insert(gearman_worker, gearman_job):
    """ registering new user """
    sys.stdout.write("[%s] :: Registering new user\n" % t)
    # convert string > datetime object
    gearman_data = json.loads(gearman_job.data)
    gearman_data.update({'datetime': parse(gearman_data['datetime'])})
    # insert data > mongo
    db.register.insert(gearman_data)
    # job done report
    sys.stdout.write("[%s] :: User registered\n" % t)
    return json.dumps(gearman_job.data)

def korban_insert(gearman_worker, gearman_job):
    """ inserting korban data """
    sys.stdout.write('[%s] :: Inserting korban data\n' % t)
    # converting string > datetime object
    gearman_data = json.loads(gearman_job.data)
    gearman_data.update({'datetime': parse(gearman_data['datetime'])})
    # inserting into mongo
    db.korban.insert(gearman_data)
    # job done report
    sys.stdout.write('[%s] :: Korban data inserted\n' % t)
    return json.dumps(gearman_job.data)

def relawan_insert(gearman_worker, gearman_job):
    """ inserting relawan data """
    sys.stdout.write('[%s] :: Inserting relawan data\n' % t)
    # converting string > datetime object
    gearman_data = json.loads(gearman_job.data)
    gearman_data.update({'datetime': parse(gearman_data['datetime'])})
    # inserting > mongo
    db.relawan.insert(gearman_data)
    # job done report
    sys.stdout.write('[%s] :: Relawan data inserted\n' % t)
    return json.dumps(gearman_job.data)


def runner(obj):
    try:
        obj.work()
    except:pass

gm_worker.set_client_id('register_new_user')
gm_worker.register_task('register', register_insert)
gm_worker.set_client_id('insert_korban')
gm_worker.register_task('korban', korban_insert)
gm_worker.set_client_id('insert_relawan')
gm_worker.register_task('relawan', relawan_insert)


while gm_worker.command_handler_holding_job_lock == None:
    runner(gm_worker)
    sleep(5)



    

