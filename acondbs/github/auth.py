"""GitHub OAuth
"""

import requests

##__________________________________________________________________||
def get_token(code, token_url, client_id, client_secret, redirect_uri):

    params = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }

    headers = {
        'Accept': "application/vnd.github.v3+json, application/json",
    }

    r = requests.post(token_url, json=params, headers=headers)
    r = r.json()
    # type(r): <class 'dict'>
    # examples:
    #   success:
    #     r = {'access_token': 'xxx', 'token_type': 'bearer', 'scope': 'user'}
    #
    #   error:
    #     r = {
    #         'error': 'bad_verification_code',
    #         'error_description': 'The code passed is incorrect or expired.',
    #         'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code'
    #     }

    token = r.get('access_token')
    return token

##__________________________________________________________________||
