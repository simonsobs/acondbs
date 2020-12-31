"""Operations on DB
"""

from flask import current_app

from .call import exchange_code_for_token

##__________________________________________________________________||
def get_github_oauth_app_info():
    ret = dict(
        authorize_url=current_app.config['GITHUB_AUTH_AUTHORIZE_URL'],
        token_url=current_app.config['GITHUB_AUTH_TOKEN_URL'],
        client_id=current_app.config['GITHUB_AUTH_CLIENT_ID'],
        client_secret = current_app.config['GITHUB_AUTH_CLIENT_SECRET'],
        redirect_uri=current_app.config['GITHUB_AUTH_REDIRECT_URI']
    )
    return ret

##__________________________________________________________________||
