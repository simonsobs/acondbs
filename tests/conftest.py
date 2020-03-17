import os
import shutil

import pytest

from acondbs import create_app

##__________________________________________________________________||
_THISDIR = os.path.dirname(os.path.realpath(__file__))

##__________________________________________________________________||
@pytest.fixture
def database_uri(tmpdir_factory):
    org_database_path = os.path.join(_THISDIR, 'product.sqlite3')
    tmpdir = str(tmpdir_factory.mktemp('instance'))
    tmp_database_path = os.path.join(tmpdir, 'product.sqlite3')
    shutil.copy2(org_database_path, tmp_database_path)
    ret = 'sqlite:///{}'.format(tmp_database_path)
    yield ret

##__________________________________________________________________||
@pytest.fixture
def app(database_uri):
    config_path = os.path.join(_THISDIR, 'config.py')
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    yield app

##__________________________________________________________________||
@pytest.fixture
def client(app):
    return app.test_client()

##__________________________________________________________________||
@pytest.fixture
def runner(app):
    return app.test_cli_runner()

##__________________________________________________________________||
