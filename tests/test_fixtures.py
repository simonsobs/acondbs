'''test global fixtures

The global fixtures are defined in `conftest.py`
'''


from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner


def test_app(app: Flask) -> None:
    '''test the fixture app'''
    assert app.testing


def test_client(client: FlaskClient) -> None:
    '''test the fixture client'''
    response = client.get('/')
    assert response


def test_runner(runner: FlaskCliRunner) -> None:
    '''test the fixture runner'''
    assert runner
