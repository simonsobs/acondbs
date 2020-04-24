from pathlib import Path

_THISDIR = Path(__file__).resolve().parent

##__________________________________________________________________||
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(_THISDIR.joinpath('product.sqlite3'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

##__________________________________________________________________||
del _THISDIR
del Path

##__________________________________________________________________||
