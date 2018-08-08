import requests
from datetime import datetime
from tzlocal import get_localzone

REFRESH_TOKEN_FILE = 'refresh_token.txt'
ACCESS_TOKEN_HOST = 'https://login.questrade.com'
ACCESS_TOKEN_ENDPOINT = '/oauth2/token'

def redeem_refresh_token(refresh_token):
    ''' Redeems the given refresh token to the questrade login server.

    Returns a json representation of the returned data which contains, among
    other things, an access token and a new refresh token.
    '''
    params = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    r = requests.post(
        ACCESS_TOKEN_HOST + ACCESS_TOKEN_ENDPOINT, 
        params=params
    )
    return r.json()

def update_refresh_token(refresh_token):
    ''' Saves the given refresh token by overriding the previous one.
    '''
    with open(REFRESH_TOKEN_FILE, 'w') as wf:
        wf.write(refresh_token)

def do_get(endpoint, params={}):
    ''' Performs a get request to the Questrade API.

    The refresh token is redeemed, giving the required access token and the
    address of the server to which to request can be sent.

    Arguments:
    endpoint    --  the webservice endpoint te request is sent to.
    params      --  the parameters to add to the request
    '''
    with open(REFRESH_TOKEN_FILE, 'r') as fr:
        refresh_token = fr.read()
    redeemed_data = redeem_refresh_token(refresh_token)
    update_refresh_token(redeemed_data['refresh_token'])
    access_token = redeemed_data['access_token']
    api_server = redeemed_data['api_server']
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    r = requests.get(api_server + endpoint, headers=headers, params=params)
    return r.json()

def add_local_tz(date):
    ''' Add the local time zone to the given date and returns a new date.

    Arguments:
    date -- a datetime object
    '''
    tz = get_localzone()
    return tz.fromutc(date.replace(tzinfo=tz))