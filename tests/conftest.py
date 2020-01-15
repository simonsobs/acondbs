# Tai Sakuma <tai.sakuma@gmail.com>
import os
import tempfile

import pytest

import sys
print(sys.path)

from acondbs import create_app

##__________________________________________________________________||
@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

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
