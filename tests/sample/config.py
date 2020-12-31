from pathlib import Path

TESTING = True
SECRET_KEY='secret_key_test_123'

##__________________________________________________________________||
_THISDIR = Path(__file__).resolve().parent

ACONDBS_DB_FOLDER = _THISDIR

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(_THISDIR.joinpath('product.sqlite3'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

ACONDBS_DB_BACKUP_PAUSE = 1.0 # second

ACONDBS_DB_BACKUP_LOCK = ACONDBS_DB_FOLDER.joinpath('.lock')
ACONDBS_DB_BACKUP_LOCK_TIMEOUT = 2.0 # second

ACONDBS_DB_BACKUP_CSV_GIT_FOLDER = _THISDIR.joinpath('db-backup-csv')
ACONDBS_DB_BACKUP_CSV_GIT_LOCK = ACONDBS_DB_BACKUP_CSV_GIT_FOLDER.joinpath('.lock')
ACONDBS_DB_BACKUP_CSV_GIT_LOCK_TIMEOUT = 2.0 # second

ACONDBS_SCHEME_MUTATION_DISABLE = False

del _THISDIR

##__________________________________________________________________||
GITHUB_AUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_AUTH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

GITHUB_AUTH_CLIENT_ID = 'client_id_0123456789'
GITHUB_AUTH_CLIENT_SECRET = 'client_secret_abcdefghijklmnupqrstuvwxyz'
GITHUB_AUTH_REDIRECT_URI = 'http://localhost:8080/signin'

GITHUB_AUTH_ADMIN_CLIENT_ID = 'client_id_0123456789'
GITHUB_AUTH_ADMIN_CLIENT_SECRET = 'client_secret_abcdefghijklmnupqrstuvwxyz'
GITHUB_AUTH_ADMIN_REDIRECT_URI = 'http://localhost:8080/signin'

##__________________________________________________________________||
GITHUB_ORG = 'test_github_org_name'

##__________________________________________________________________||
del Path

##__________________________________________________________________||
