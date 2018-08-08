import utils

def get_time():
	'''Retrieve current server time.
	'''
	return utils.do_get('v1/time')

def get_accounts():
	'''Retrieves the accounts associated with the user on behalf of which the 
	API client is authorized.
	'''
	return utils.do_get('v1/accounts')

def get_positions(id):
	''' Retrives positions in a specified account.

	Arguments:
	id (String)	--	Account number
	'''
	return utils.do_get('v1/accounts/{}/positions'.format(id))

def get_balances(id):
	''' Retrieves per-currency and combined balances for a specified account.

	Arguments:
	id (String)	--	Account number
	'''
	return utils.do_get('v1/accounts/{}/balances'.format(id))

def get_executions(id, start_time=None, end_time=None):
	''' Retrieves executions for a specific account.

	Arguments:
	id (String)				--	Account number
	start_time (datetime)	--	Start of the time range (default today 00:00am)
	end_time (datetime)		--	End of the time range (default todat 11:59pm)
	'''
	params = {}
	if start_time:
		params.update({'startTime': utils.add_local_tz(start_time)})
	if end_time:
		params.update({'end_time': utils.add_local_tz(end_time)})
	return utils.do_get('v1/accounts/{}/executions'.format(id), params)

def get_orders(id, state_filter=None, start_time=None, 
			   end_time=None, order_ids=None):
	''' Retrieves orders for a specified account.

	Arguments:
	id (String)				--	Account number
	state_filter (String)	--	'All', 'Open' or 'Closed'. Retreive all, active
								or closed orders. (default 'All')
	start_time (datetime)	--	Start of the time range (default today 00:00am)
	end_time (datetime)		--	End of the time range (default todat 11:59pm)
	order_ids (int list)	--	Retrieve specific orders details	
	'''
	params={}
	if start_time:
		params.update({'startTime': utils.add_local_tz(start_time)})
	if end_time:
		params.update({'endTime': utils.add_local_tz(end_time)})
	if state_filter:
		params.update({'stateFilter': state_filter})
	if order_ids:
		params.update({'ids': ','.join(map(str, order_ids))})
	return utils.do_get('v1/accounts/{}/orders'.format(id), params)

def get_activities(id, start_time=None, end_time=None):
	''' Retrieve account activities, including cash transactons, dividends,
	trades, etc.

	Arguments:
	id (String)				--	Account number
	start_time (datetime)	--	Start of the time range (default today 00:00am)
	end_time (datetime)		--	End of the time range (default todat 11:59pm)
	'''
	params={}
	if start_time:
		params.update({'startTime': utils.add_local_tz(start_time)})
	if end_time:
		params.update({'endTime': utils.add_local_tz(end_time)})
	return utils.do_get('v1/accoutns/{}/activities'.format(id), params)

def get_symbols(names=None, ids=None, id=None):
	''' Retrieves detailed information about one or more symbol.

	Arguments:
	name (String list)	--	List of symbol names
	ids (int list)		-- 	List of symbol ids
	id (int)			-- 	Internal symbol identifier. Mutially exclusive with 
							'ids' parameter

	Either list of names or ids can be specified, but not both. If 'names' is
	specified, it takes precedence over 'ids', which takes precedence over 'id'.
	'''
	params={}
	endpoint = 'v1/symbols'
	if names:
		params.update({'names': ','.join(map(str, names))})
	elif ids:
		params.update({'ids': ','.join(map(str, ids))})
	elif id:
		endpoint += '/' + str(id)
	return utils.do_get(endpoint, params)



'''
DEV TESTING
'''
from datetime import datetime

# id = get_accounts()['accounts'][0]['number']
# oid = get_orders(id, start_time=datetime(2018,1,1))['orders'][0]['id']

# id = '51615667'
# oid1 = 439302957
# oid2 = 439302960

# r = get_orders(id, order_ids=(oid1,oid2))
id1 = 17473
id2 = 16529510
id2 = 8049

r = get_symbols(names='GOOG')