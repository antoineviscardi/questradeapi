API
===

Thorough documentation of the different available API calls can be found on Questrade's website `here <https://www.questrade.com/api/documentation/rest-operations/>`__. 

Enumeration Values
------------------
Some API calls' parameters only accept specific string values. A list of those enumerations and their description can be found `here <https://www.questrade.com/api/documentation/rest-operations/enumerations/enumerations>`__ on Questrade's website.

Data Structures
---------------
Some API calls' parameters requires :obj:`dict` of a specific structure to be passed. These data structures and utility methods to create them are documented in the :ref:`data-structures` section.



.. module:: questradeapi

Account Calls
-------------
.. automethod:: Session.get_time
.. automethod:: Session.get_accounts
.. automethod:: Session.get_positions
.. automethod:: Session.get_balances
.. automethod:: Session.get_executions
.. automethod:: Session.get_orders
.. automethod:: Session.get_activities

Market Calls
------------
.. automethod:: Session.get_symbols
.. automethod:: Session.get_symbols_search
.. automethod:: Session.get_option_chain
.. automethod:: Session.get_markets
.. automethod:: Session.get_quotes
.. automethod:: Session.get_quotes_options
.. automethod:: Session.get_quotes_strategies
.. automethod:: Session.get_candles

Order Calls
-----------
.. automethod:: Session.post_order
.. automethod:: Session.delete_order
.. automethod:: Session.post_bracket_order
.. automethod:: Session.post_multi_leg_strategy_order
