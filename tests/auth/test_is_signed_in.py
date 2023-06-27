from typing import Any

from flask import Flask

from acondbs import auth


def test_true(app: Flask) -> None:
    token = '90b2ee5fed25506df04fd37343bb68d1803dd97f'
    environ_base = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
    with app.test_request_context(environ_base=environ_base):
        assert auth.is_signed_in()


def test_false_wrong_token(app: Flask) -> None:
    token = '0000000000000000000000000000000000000000'
    environ_base = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
    with app.test_request_context(environ_base=environ_base):
        assert not auth.is_signed_in()


def test_false_no_token(app: Flask) -> None:
    environ_base: dict[str, Any] = {}
    with app.test_request_context(environ_base=environ_base):
        assert not auth.is_signed_in()
