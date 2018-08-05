from enum import Enum
import requests

REFRESH_TOKEN_FILE = 'refresh_token.txt'
ACCESS_TOKEN_HOST = 'https://login.questrade.com'
ACCESS_TOKEN_ENDPOINT = '/oauth2/token'


def redeem_refresh_token(refresh_token):
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
	with open(REFRESH_TOKEN_FILE, 'w') as wf:
		wf.write(refresh_token)


with open(REFRESH_TOKEN_FILE, 'r') as fr:
	refresh_token = fr.read()


redeemed_data = redeem_refresh_token(refresh_token)

update_refresh_token(redeemed_data['refresh_token'])

# # access_token = get_access_token(refresh_token)
# rr = access_token = get_access_token(refresh_token)
# headers = {'Authorization': 'Bearer {}'.format(access_token)}
# r = requests.get(
# 	'https://api07.iq.questrade.com/v1/accounts', 
# 	headers=headers
# )
# r = requests.get('https://api01.iq.questrade.com/v1/time')


