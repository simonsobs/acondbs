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

    config_path = os.path.join(_THISDIR, 'config.py')
    app = create_app(config_path)

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
