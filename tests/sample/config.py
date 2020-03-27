import os

_THISDIR = os.path.dirname(os.path.realpath(__file__))

##__________________________________________________________________||
TESTING = True,
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(_THISDIR, 'product.sqlite3'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

##__________________________________________________________________||
del _THISDIR
del os

##__________________________________________________________________||
