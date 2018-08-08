import requests
import time
import json
from datetime import datetime
from tzlocal import get_localzone

TOKEN_FILE = 'token.json'
ACCESS_TOKEN_HOST = 'https://login.questrade.com'
ACCESS_TOKEN_ENDPOINT = '/oauth2/token'

def get_access_data():
    '''Returns the data required to access the server, namely a access token and
    the api server's address in a tuple.

    If the access token is expired, the refresh token is redeemed.
    '''
    with open(TOKEN_FILE, 'r') as f:
        token_data = json.load(f)
    now = time.time()
    expires_at = token_data.get('expires_at', 0)
    if now > expires_at:
        token_data = redeem_refresh_token(token_data['refresh_token'])
        with open(TOKEN_FILE, 'w') as f:
            json.dump(token_data, f)
    return (token_data['access_token'], token_data['api_server'])

def redeem_refresh_token(refresh_token):
    ''' Redeems the given refresh token to the questrade login server and 
    returnes the received data.

    Prior to returning the data, the expiry time of the access token is computed 
    and added to the data.
    '''
    params = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    r = requests.post(
        ACCESS_TOKEN_HOST + ACCESS_TOKEN_ENDPOINT, 
        params=params
    )
    json_data = r.json()
    expires_at = time.time() + json_data['expires_in']
    json_data['expires_at'] = expires_at
    return json_data

def do_get(endpoint, params={}):
    ''' Performs a get request to the Questrade API.

    Arguments:
    endpoint    --  the webservice endpoint te request is sent to.
    params      --  the parameters to add to the request
    '''
    access_token, api_server = get_access_data()
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