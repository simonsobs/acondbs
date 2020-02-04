import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

##__________________________________________________________________||
db = SQLAlchemy()

##__________________________________________________________________||
def get_db_connection():
    if 'db' not in g:
        g.db = db.engine.connect()
    return g.db

##__________________________________________________________________||
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

##__________________________________________________________________||
def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
    app.teardown_appcontext(close_db)

##__________________________________________________________________||
def init_db():
    pass

##__________________________________________________________________||
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

##__________________________________________________________________||
