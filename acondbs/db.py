import click
from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy

##__________________________________________________________________||
_db = SQLAlchemy()

##__________________________________________________________________||
def get_db():
    if 'db' not in g:
        g.db = _db.engine.connect()
    return g.db

##__________________________________________________________________||
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

##__________________________________________________________________||
def init_app(app):
    _db.init_app(app)
    app.teardown_appcontext(close_db)

##__________________________________________________________________||
