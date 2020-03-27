import os
import shutil

import pytest

from acondbs import create_app

##__________________________________________________________________||
_THISDIR = os.path.dirname(os.path.realpath(__file__))

##__________________________________________________________________||
@pytest.fixture
def database_uri(tmpdir_factory):
    """the database URI for a temporarily copy of the test data

    The fixture copies the test data `product.sqlite3` to a
    temporarily folder and returns the URI for the copy.

    """
    org_database_path = os.path.join(_THISDIR, 'product.sqlite3')
    tmpdir = str(tmpdir_factory.mktemp('instance'))
    tmp_database_path = os.path.join(tmpdir, 'product.sqlite3')
    shutil.copy2(org_database_path, tmp_database_path)
    ret = 'sqlite:///{}'.format(tmp_database_path)
    yield ret

##__________________________________________________________________||
@pytest.fixture
def app(database_uri):
    """a test Flask application
    """
    config_path = os.path.join(_THISDIR, 'config.py')
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    yield app

##__________________________________________________________________||
@pytest.fixture
def client(app):
    """a test client of the Flask application

    The test client can emulate HTTP requests, e.g, GET, POST. More in
    the Flask documentation:
    https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client

    """
    yield app.test_client()

##__________________________________________________________________||
@pytest.fixture
def runner(app):
    """a test CLI runner of the Flask application

    The runner is used to test custom click commands. More in the
    Flask documentation:
    https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_cli_runner

    """
    yield app.test_cli_runner()

##__________________________________________________________________||
