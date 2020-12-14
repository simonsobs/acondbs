"""GitHub OAuth
"""

from flask import current_app
import requests

##__________________________________________________________________||
def get_token(code, admin=False):

    token_url = current_app.config['GITHUB_AUTH_TOKEN_URL']

    if admin:
        github_client_id = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_ID']
        github_client_secret = current_app.config['GITHUB_AUTH_ADMIN_CLIENT_SECRET']
        redirect_uri = current_app.config['GITHUB_AUTH_ADMIN_REDIRECT_URI']
    else:
        github_client_id = current_app.config['GITHUB_AUTH_CLIENT_ID']
        github_client_secret = current_app.config['GITHUB_AUTH_CLIENT_SECRET']
        redirect_uri = current_app.config['GITHUB_AUTH_REDIRECT_URI']

    params = {
        'grant_type': 'authorization_code',
        'client_id': github_client_id,
        'client_secret': github_client_secret,
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
