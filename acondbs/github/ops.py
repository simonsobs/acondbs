"""Operations on DB
"""

from flask import current_app

from . import call

##__________________________________________________________________||
def get_github_oauth_app_info():
    ret = dict(
        authorize_url=current_app.config['GITHUB_AUTH_AUTHORIZE_URL'],
        token_url=current_app.config['GITHUB_AUTH_TOKEN_URL'],
        client_id=current_app.config['GITHUB_AUTH_CLIENT_ID'],
        client_secret=current_app.config['GITHUB_AUTH_CLIENT_SECRET'],
        redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
    )
    return ret

##__________________________________________________________________||
def exchange_code_for_token(code):
    oauth_app_info = get_github_oauth_app_info()
    return call.exchange_code_for_token(
        code,
        token_url=oauth_app_info['token_url'],
        client_id=oauth_app_info['client_id'],
        client_secret=current_app.config['GITHUB_AUTH_CLIENT_SECRET'],
        redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
        )

##__________________________________________________________________||
