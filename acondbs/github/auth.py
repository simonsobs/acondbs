"""GitHub OAuth
"""

import requests

##__________________________________________________________________||
def get_token(code, token_url, client_id, client_secret, redirect_uri):
    """exchange a code for an access token

    https://docs.github.com/en/free-pro-team@latest/developers/apps/authorizing-oauth-apps#2-users-are-redirected-back-to-your-site-by-github
    """

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

    response = requests.post(token_url, json=params, headers=headers)
    response = response.json()
    # type(response): <class 'dict'>
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

    token = response.get('access_token')
    return token

##__________________________________________________________________||
