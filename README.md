# Questrade API Wrapper
This package is a Python wrapper for the [Questrade API][api].

## Under construction

## TODO
- Test from def_searchs
- Implement unit tests
- Define and document the different enumeration values.
- default values for enums?
- Access expiry buffer? 

## Installation
To install QuestradeAPI, you can use [pipenv][pipenv] (or pip, of course):
```
pip install questradeapi
```

## Usage
For a list and an in depth descriptions of the different API requests and responses, you can check out Questrade's documentation on the subject [here][api-methods]. 

To use the python wrapper, you need to create a session providing a refresh token. The session object can then be used to perform API requests.
```
import questradeapi as qapi
sess = qapi.Session('some_token_42')

```
### GET time
Retrieve current server time.
```
r = sess.get_time()
```

### GET accounts
Retrieves the accounts associated with the user on behalf of which the API client is authorized.
```
r = sess.get_accounts()
```

### GET accounts/:id/positions
Retrives positions in a specified account.
```
r = sess.get_positions(id)
```

## Issue Reporting
I you find a bug, have a feature request, or have design suggestions, please do not hesitate to report it in the issues section of this repository. For any security related issues, please do not report them publicly on the public GitHub issue tracker but contact me direcly by email.

## Author
[Antoine Viscardi][avis]

[api]: https://www.questrade.com/api/documentation/getting-started
[api-methods]: https://www.questrade.com/api/documentation/rest-operations/
[pipenv]: https://docs.pipenv.org/

[avis]: https://antoineviscardi.github.io