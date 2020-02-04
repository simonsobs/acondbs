import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

##__________________________________________________________________||
db = SQLAlchemy()

##__________________________________________________________________||
def get_db_connection():
    if 'db_connection' not in g:
        g.db_connection = db.engine.connect()
    return g.db_connection

##__________________________________________________________________||
def close_db_connection(e=None):
    conn = g.pop('db_connection', None)
    if conn is not None:
        conn.close()

##__________________________________________________________________||
def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
    app.teardown_appcontext(close_db_connection)

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
