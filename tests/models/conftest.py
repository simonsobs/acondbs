import pytest
from flask import Flask

from acondbs import create_app
from acondbs.db.ops import define_tables


@pytest.fixture
def app_empty() -> Flask:
    database_uri = 'sqlite:///:memory:'
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()

    return y
