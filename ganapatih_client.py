import gearman
import json

d = {
    'nama': 'hiraq',
    'alamat': 'yojo',
    'notelp': '303030303',
    'status': 'relawan',
    'timestamp': '2013-02-18 08:55:31',
    }

client = gearman.GearmanClient(['127.0.0.1'])
print 'sending data'

register_request = client.submit_job('register', json.dumps(d))
korban_request = client.submit_job('korban', json.dumps(d))
relawan_request = client.submit_job('relawan', json.dumps(d))

register_result = register_request.result
korban_result = korban_request.result
relawan_result = relawan_request.result

print register_result
print korban_result
print relawan_result
