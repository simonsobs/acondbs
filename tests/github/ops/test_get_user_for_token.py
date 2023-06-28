import pytest
import sqlalchemy
from flask import Flask

from acondbs.github import ops


def test_success(app: Flask) -> None:
    token = 'token3'
    with app.app_context():
        user = ops.get_user_for_token(token)
    assert 'user2' == user.login


def test_error(app: Flask) -> None:
    token = 'no-such-token'
    with app.app_context():
        with pytest.raises(sqlalchemy.orm.exc.NoResultFound):
            _ = ops.get_user_for_token(token)
