import pytest
from flask import Flask


@pytest.fixture
def app(app_empty: Flask) -> Flask:
    y = app_empty
    return y
