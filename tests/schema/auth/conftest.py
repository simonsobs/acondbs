import pytest
from flask import Flask


@pytest.fixture
def app(app_users: Flask) -> Flask:
    y = app_users
    return y
