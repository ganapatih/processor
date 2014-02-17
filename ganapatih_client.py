import gearman
import json

d = {
    'nama': 'roland',
    'alamat': 'krapyak coret',
    'notelp': '303030303',
    'status': 'feeling blue'
    }

new_client = gearman.GearmanClient(['127.0.0.1'])
print 'sending data'
current_request = new_client.submit_job('register', json.dumps(d))
new_result = current_request.result
