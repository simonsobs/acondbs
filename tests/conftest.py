# Tai Sakuma <tai.sakuma@gmail.com>
import os
import tempfile

import pytest

import sys
from acondbs import create_app

##__________________________________________________________________||
_THISDIR = os.path.dirname(os.path.realpath(__file__))

##__________________________________________________________________||
@pytest.fixture
def app():

    config = dict(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(_THISDIR, 'acl.sqlite3')),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    app = create_app(config)

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
