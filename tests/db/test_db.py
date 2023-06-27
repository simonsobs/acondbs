from flask import Flask


def test_init_app(app: Flask) -> None:
    '''test if the Flask app is initialized for the DB'''

    # not clearly exactly how to test.
    # just check if 'sqlalchemy' in the extensions
    assert 'sqlalchemy' in app.extensions
