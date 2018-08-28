Quick Start
===========
Prerequisites
-------------
If you are reading this quick start guide, it is assumed that you have an active Questrade trading account with which to use the API. If this is not the case, then I don't know what you are doing here ¯\\_(ツ)_/¯.

Setup
-----
In order to acces Questrade's API, you need to authorize your application to use the API through your account. This can be done by following `this guide <https://www.questrade.com/api/documentation/getting-started>`__ from Questrade.
Once this is done, you should be able to generate refresh tokens. This is important because you will need to feed one of those token to the Session in order to be able to perform API calls.

Using the API
-------------
A :obj:`Sessions` is used to make the different API calls. Given an initial refresh token, it automatically deals with the redeeming process to get access tokens.

The following code snippet initializes a session with a refresh token and performs some simple API calls. 

.. code-block:: python

	import questradeapi as qapi

	refresh_token = input('Refresh Token: ')
	sess = qapi.Session(refresh_token)

	id = sess.get_accounts()['accounts'][0]['number'] #Fetch first account ID.
	positions = sess.get_positions(id)
	balances = sess.get_balances(id)

