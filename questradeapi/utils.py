from tzlocal import get_localzone

def add_local_tz(date):
    ''' Add the local time zone to the given date and returns a new date.

    Parameters
    ----------
    date : :obj:`datetime`
        Date to which to adjust with the local time zone.

    Returns
    -------
    :obj:`datetime`
        Date adjusted with local timezone.
  
    '''
    tz = get_localzone()
    return tz.fromutc(date.replace(tzinfo=tz))

def create_option_id_filter(option_type, underlying_id, expiry_date, 
                            min_strike_price, max_strike_price):
    ''' Simple utility to generate an OptionIdFilter structure.

    Parameters
    ----------
    option_type : :obj:`str`, {'Call', 'Put'}
        Option type.
    underlying_id : :obj:`int`
        Underlying ID.
    expiry_date : :obj:`datetime`
        Expiry date.
    min_strike_price : :obj:`double`
        Min strike price.
    max_strike_price : :obj:`double`
        Max strike price.

    Note
    ----
    More details on allowed `option_type` values can be found `here 
    <https://www.questrade.com/api/documentation/rest-operations/enumerat \
    ions/enumerations#option-type>`__.

    Returns
    -------
    :obj:`dict`
        OptionIdFilter structure.

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
    ''' Simple utility to generate a StrategyVariantRequest structure.

    Parameters
    ----------
    variant_id : :obj:`int`
        Variant ID.
    strategy : :obj:`str`, {'CoveredCall', 'MarriedPuts', \
    'VerticalCallSpread', 'VerticalPutSpread', 'CalendarCallSpread', \
    'CalendarPutSpread', 'DiagonalCallSpread', 'DiagonalPutSpread', 'Collar', \
    'Straddle', 'Strangle', 'ButterflyCall', 'ButterflyPut', 'IronButterfly', \
    'CondorCall', 'Custom'}
        Strategy type.
    legs : :obj:`list` of :obj:`dict`
        List of StrategyVariantLeg structures.

    Note
    ----
    More details on allowed `strategy` values can be found `here \
    <https://www.questrade.com/api/documentation/rest-operations/enumerations/ \
    enumerations#strategy-types>`__.

    Returns
    -------
    :obj:`dict`
        StrategyVariantRequest structure.

    '''
    strategy_variant_request = {
        'variantId': variant_id,
        'strategy': strategy,
        'legs': legs
    }
    return strategy_variant_request

def create_strategy_variant_leg(symbol_id, action, ratio):
    ''' Simple utility function to generate a StrategyVariantLeg structure.

    Parameters
    ----------
    symbolId : :obj:`int`
        Internal symbol identifier.
    action : :obj:`str`, {'Buy', 'Sell'}
        Order side.
    ratio : :obj:`int`
        Numeric ration of the leg strategy.

    Note
    ----
    More details on allowed `action` values can be found `here 
    <https://www.questrade.com/api/documentation/rest-operations/enumerations/ \
    enumerations#order-action>`__.

    Returns
    -------
    :obj:`dict`
        StrategyVariantLeg structure.

    '''
    strategy_variant_leg = {
        'symbolId': symbol_id,
        'acton': action,
        'ratio': ratio
    }
    return strategy_variant_leg

def create_bracket_order_component(quantity, action, limit_price, stop_price, 
                                   order_type, time_in_force, order_class, 
                                   order_id=0):
    ''' Simple utility to generate a BracketOrderComponent structure.

    Parameters
    ----------
    quantity : :obj:`double`
        Order quantity.
    action : :obj:`str`, {'Buy', 'Sell'}
        Order side.
    limit_price : :obj:`double`
        Limit price.
    stop_price : :obj:`double`
        Stop price.
    order_type : :obj:`str`, {'Market', 'Limit', 'Stop', 'StopLimit', \
    'TrailStopInPercentage', 'TrailStopInDollar', \
    'TrailStopLimitInPercentage', 'TrailStopLimitInDollar', 'LimitOnOpen', \
    'LimitOnClose'}
        Order type.
    time_in_force : :obj:`str`, {'Day', 'GoodTillCanceled', \
    'GoodTillExtendedDay', 'GoodTillDate', 'ImmediateOrCancel', 'FillOrKill'}
        Order duration.
    order_class : :obj:`str`, {'Primary', 'Limit', 'StopLoss'}
        Type of component

    Note
    ----
    More details on allowed `action`, `order_type`, `time_in_force` and 
    `order_class` can be found `here <https://www.questrade.com/api/ \
    documentation/rest-operations/enumerations/enumerations>`__

    Returns
    -------
    :obj:`dict`
        BracketOrderComponent structure.

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
    ''' Simple utililty function to generate a InsertOrderLegData structure.

    Parameters
    ----------
    symbol_id : :obj:`int`
        Internal symbol identifier.
    action : :obj:`str`, {'Buy', 'Sell'}
        Leg action.
    leg_quantity : :obj:`int`
        Leg quantity.

    Note
    ----
    More details on allowed `action` values can be found `here 
    <https://www.questrade.com/api/documentation/rest-operations/enumerations/ \
    enumerations#order-action>`__.

    Returns
    -------
    :obj:`dict`
        InsertOrderLegData structure.

    '''
    insert_order_leg_data = {
        'symbolId': symbol_id,
        'action': action,
        'legQuantity': leg_quantity
    }
    return insert_order_leg_data
