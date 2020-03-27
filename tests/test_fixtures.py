"""test global fixtures

The global fixtures are defined in `conftest.py`
"""

##__________________________________________________________________||
def test_app(app):
    """test the fixture app
    """
    from flask import Flask
    assert isinstance(app, Flask)
    assert app.testing

##__________________________________________________________________||
