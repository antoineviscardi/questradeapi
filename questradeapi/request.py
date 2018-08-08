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
		if isinstance(names, str):
			params.update({'names': names})
		else:
			params.update({'names': ','.join(names)})
	elif ids:
		params.update({'ids': ','.join(map(str, ids))})
	elif id:
		endpoint += '/' + str(id)
	return utils.do_get(endpoint, params)

def search(prefix, offset=None):
	''' Retrieves symbol(s) using several search criteria.

	Arguments:
	prefix (String)	--	Prefix of a symbol or any word in the description
	offset (int)	--	Offset in number of records from the beginning of a 
						result set.
	'''
	params={'prefix': prefix}
	if offset:
		params.update({'offset': offset})
	return utils.do_get('v1/symbols/search', params)

def get_option_chain(id):
	'''Retrieves an option chain for a particular underlying symbol.

	Arguments:
	id (int)	--	Internal symbol identifier
	'''
	return utils.do_get('v1/symbols/{}/options'.format(id))

def get_markets():
	'''Retrieves information about supported markets.
	'''
	return utils.do_get('v1/markets')

def get_quotes(id=None, ids=None):
	'''Retrieves a single Level 1 market data quote for one or more symbols.

	Arguments:
	id (int)		--	Internal symbol identifier (mutually exclusive with 
						'ids' argument)
	ids (int list)	--	Comman-separated list of symbol ids
	'''
	endpoint = 'v1/markets/quotes'
	if id:
		endpoint += '/' + str(id)
		return utils.do_get(endpoint)
	else:
		params = {'ids': ','.join(map(str, ids))}
		return utils.do_get(endpoint, params)

def get_quotes_options(filters=None, ids=None):
	''' Retrieves a single Level 1 market data quote and Greek data for one or
	more option symbols.

	Arguments:
	filters (dic list)	--	Array of OptionIdFilter structures
	ids (int list)		--	Array of option IDs

	OptionIdFilter structures:
	optionType (list)		--	Option type
	underlyingId (int)		--	Underlying ID
	expiryDate (datetime)	--	Expiry date
	minstrikePrice (double)	--	Min strike price
	maxstrikePrice (double)	--	Max strike price
	'''
	pass

def get_quotes_strategies(variants):
	'''Retrieve a calculated L1 market data quote for a single or many multi-leg
	strategies.
	
	Arguments:
	variants (dic list)	--	Array of Strategy Variants

	StrategyVariantRequest:
	variantId (int)	--	Variant ID
	strategy (enum)	--	Strategy type 
	legs (dic list)	--	Array of Strategy legs

	StrategyLeg:
	symbolId (int)	--	Internal symbol identifier
	action (enum)	--	Order side
	ratio (int)		--	Numeric ration of the leg strategy
	'''
	pass

def get_candles(id, start_time, end_time, interval):
	'''Retrieves historical market data in the form of OHLC candlesticks for a 
	specified symbol. This call is limited to returning 2,000 candlesticks in
	a single response.

	Arguments:
	id (int)				--	Internal symbol indentifier
	startTime (datetime)	--	Beginning of the candlestick range
	endTime (datetime)		--	End of the candlestick range
	interval (enum)			--	Interval of a single candlestick
	'''
	params = {
		'startTime': utils.add_local_tz(start_time),
		'endTime': utils.add_local_tz(end_time), 
		'interval': interval
	}
	return utils.do_get('v1/markets/candles/{}'.format(id), params)

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
