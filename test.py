'''
DEV TESTING
'''

import questradeapi as qapi
from datetime import datetime

refresh_token = input('Refresh Token: ')
sess = qapi.Session(refresh_token)

id = sess.get_accounts()['accounts'][0]['number']
# oid = get_orders(id, start_time=datetime(2018,1,1))['orders'][0]['id']

# id = '51615667'
# oid1 = 439302957
# oid2 = 439302960

# r = get_orders(id, order_ids=(oid1,oid2))
id1 = 17473
id2 = 16529510
id2 = 8049


