from tzlocal import get_localzone

def add_local_tz(date):
    ''' Add the local time zone to the given date and returns a new date.

    Arguments:
    date -- a datetime object
    '''
    tz = get_localzone()
    return tz.fromutc(date.replace(tzinfo=tz))

def create_option_id_filter(option_type, underlying_id, expiry_date, 
                            min_strike_price, max_strike_price):
    ''' Simple utility function to generate an OptionIdFilter structure as 
    required by the GET markets/quotes/options API call.

    Arguments:
    option_type (enum)          --  Option type
    underlying_id (int)         --  Underlying ID
    expiry_date (datetime)      --  Expiry date
    min_strike_price (double)   --  Min strike price
    max_strike_price (double)   --  Max strike price
    '''
    option_id_filter = {
        'optionType': option_type,
        'underlyingId': underlying_id,
        'expiry_date': expiry_date,
        'minStrikePrice': min_strike_price,
        'maxStrikePrice': maxStrikePrice
    }
    return option_id_filter

def create_strategy_variant_request(variant_id, strategy, legs):
    ''' Simple utility function to generate a StrategyVariantRequest structure
    as required by the Get markets/quotes/strategies API call.

    Arguments:
    variant_id (int)    --  Variant ID
    strategy (enum)     --  Strategy type 
    legs (dic list)     --  Array of Strategy legs
    '''
    strategy_variant_request = {
        'variantId': variant_id,
        'strategy': strategy,
        'legs': legs
    }
    return strategy_variant_request

def create_strategy_variant_leg(symbol_id, action, ratio):
    ''' Simple utility function to generate a StrategyVariantLeg structure as
    required by the StrategyVariantRequest structure.

    Arguments:
    symbolId (int)  --  Internal symbol identifier
    action (enum)   --  Order side
    ratio (int)     --  Numeric ration of the leg strategy
    '''
    strategy_variant_leg = {
        'symbolId': symbol_id,
        'acton': action,
        'ratio': ratio
    }
    return strategy_variant_leg

def create_bracket_order_component(quantity, action, limit_price, stop_price, 
                                   order_type, time_in_force, ordre_class, 
                                   order_id=0):
    ''' Simple utility function to generate a Component for a bracket order as
    required by the POST accounts/:id/orders/bracket[/impact] API call.

    Arguments:
    quantity (double)       --  Order quantity
    action (enum)           --  Order side
    limit_price (double)    --  Limit price
    stop_price (double)     --  Stop price
    order_type (enum)       --  Order type
    time_in_force (enum)    --  Order duration
    ordre_class (enum)      --  Type of component
    '''
    bracket_order_component = {
        'orderId': order_id,
        'quantity': quantity, 
        'action': action, 
        'limitPrice': limit_price, 
        'stopPrice': stop_price,
        'orderType': order_type,
        'timeInForce': time_in_force,
        'orderClass': order_class
    }
    return bracket_order_component

def create_insert_order_leg_data(symbol_id, action, leg_quantity):
    ''' Simple utililty function to generate a InsertOrderLegData structure as
    required by the accounts/:id/orders/strategy[/impact] API call.

    Arguments:
    symbol_id (int)     --  Internal symbol identifier
    action (enum)       --  Leg action
    leg_quantity (int)  --  Leg quantity
    '''
    insert_order_leg_data = {
        'symbolId': symbol_id,
        'action': action,
        'legQuantity': leg_quantity
    }
    return insert_order_leg_data
