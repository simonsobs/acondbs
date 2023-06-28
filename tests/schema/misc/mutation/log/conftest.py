import pytest
from flask import Flask

from acondbs import ops


@pytest.fixture
def app(app_users: Flask) -> Flask:
    y = app_users

    with y.app_context():
        ops.create_log(id_=1, level="DEBUG", message="A debug message!")
        ops.create_log(id_=2, level="ERROR", message="An error message!")
        ops.commit()

    return y
