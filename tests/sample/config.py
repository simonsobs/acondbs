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

##__________________________________________________________________||
del _THISDIR
del Path

##__________________________________________________________________||
