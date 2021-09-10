"""test global fixtures

The global fixtures are defined in `conftest.py`
"""


##__________________________________________________________________||
def test_app(app):
    """test the fixture app"""
    from flask import Flask

    assert isinstance(app, Flask)
    assert app.testing


##__________________________________________________________________||
def test_client(client):
    """test the fixture client"""
    response = client.get("/")
    assert response


##__________________________________________________________________||
def test_runner(runner):
    """test the fixture runner"""
    assert runner


##__________________________________________________________________||
