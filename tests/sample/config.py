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
GITHUB_AUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_AUTH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

GITHUB_AUTH_CLIENT_ID = '0123456789abcdefghij'
GITHUB_AUTH_CLIENT_SECRET = 'abcdefghijklmnupqrstuvwxyz0123456789abcd'
GITHUB_AUTH_REDIRECT_URI = 'http://localhost:8080/signin'

GITHUB_AUTH_ADMIN_CLIENT_ID = 'abcdefghij0123456789'
GITHUB_AUTH_ADMIN_CLIENT_SECRET = '0123456789abcdefghijklmnupqrstuvwxyz0123'
GITHUB_AUTH_ADMIN_REDIRECT_URI = 'http://localhost:8080/admin/signin'

##__________________________________________________________________||
del _THISDIR
del Path

##__________________________________________________________________||
