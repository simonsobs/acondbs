import os
import ast
from pathlib import Path

try:

    _PARENT_DIR = Path(__file__).resolve().parent.parent

    ##______________________________________________________________||
    SECRET_KEY = os.environ.get('ACONDBS_SECRET_KEY')

    ##______________________________________________________________||
    ACONDBS_DB_FOLDER = Path(os.environ.get('ACONDBS_DB_FOLDER'))

    ##______________________________________________________________||
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ACONDBS_DB_BACKUP_PAUSE = 60.0 # second

    ACONDBS_DB_BACKUP_LOCK = ACONDBS_DB_FOLDER.joinpath('.lock')
    ACONDBS_DB_BACKUP_LOCK_TIMEOUT = 30.0 # second

    ACONDBS_DB_BACKUP_CSV_GIT_FOLDER = _PARENT_DIR.joinpath('db-backup-csv')
    ACONDBS_DB_BACKUP_CSV_GIT_LOCK = ACONDBS_DB_BACKUP_CSV_GIT_FOLDER.joinpath('.lock')
    ACONDBS_DB_BACKUP_CSV_GIT_LOCK_TIMEOUT = 30.0 # second

    ##______________________________________________________________||
    ACONDBS_OWNERS_GITHUB_LOGINS = os.environ.get('ACONDBS_OWNERS_GITHUB_LOGINS') # comma separated e.g., "octocat,dojocat"

    ##______________________________________________________________||
    ACONDBS_GRAPHIQL = ast.literal_eval(os.environ.get('ACONDBS_GRAPHIQL', 'True'))
    ACONDBS_GRAPHIQL_TEMPLATE_NO = ast.literal_eval(os.environ.get('ACONDBS_GRAPHIQL_TEMPLATE_NO', 'None')) # None: default, 1: GraphiQL latest, 2: GraphQL Playground

    ##______________________________________________________________||
    GITHUB_AUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
    GITHUB_AUTH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

    GITHUB_AUTH_CLIENT_ID = os.environ.get('GITHUB_AUTH_CLIENT_ID')
    GITHUB_AUTH_CLIENT_SECRET = os.environ.get('GITHUB_AUTH_CLIENT_SECRET')
    GITHUB_AUTH_REDIRECT_URI = os.environ.get('GITHUB_AUTH_REDIRECT_URI')

except Exception as e:
    print(e)

##__________________________________________________________________||
del _PARENT_DIR
del Path
del os
del ast

##__________________________________________________________________||
