"""test global fixtures

The global fixtures are defined in `conftest.py`
"""


def test_app(app):
    """test the fixture app"""
    from flask import Flask

    assert isinstance(app, Flask)
    assert app.testing


def test_client(client):
    """test the fixture client"""
    response = client.get("/")
    assert response


def test_runner(runner):
    """test the fixture runner"""
    assert runner
