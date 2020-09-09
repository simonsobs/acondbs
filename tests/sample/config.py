from pathlib import Path

_THISDIR = Path(__file__).resolve().parent

##__________________________________________________________________||
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(_THISDIR.joinpath('product.sqlite3'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

ACONDBS_DB_BACKUP_CSV_GIT_FOLDER = _THISDIR.joinpath('db-backup-csv')
ACONDBS_DB_BACKUP_CSV_GIT_PAUSE = 1.0 # second
ACONDBS_DB_BACKUP_CSV_GIT_LOCK = ACONDBS_DB_BACKUP_CSV_GIT_FOLDER.joinpath('.lock')
ACONDBS_DB_BACKUP_CSV_GIT_LOCK_TIMEOUT = 2.0 # second

ACONDBS_SCHEME_MUTATION_DISABLE = False

##__________________________________________________________________||
GITHUB_AUTH_CLIENT_ID = '1ce266dd301a653ca64f'
GITHUB_AUTH_CLIENT_SECRET = 'adb99c5ef0cdfbc052af1e3573684026bd2c1c23'
GITHUB_AUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_AUTH_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_AUTH_REDIRECT_URI = 'http://localhost:8081/signin'

##__________________________________________________________________||
del _THISDIR
del Path

##__________________________________________________________________||
