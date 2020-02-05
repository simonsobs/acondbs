import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import json

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
    app.cli.add_command(dump_db_command)
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
def get_all_db_content():
    # https://stackoverflow.com/questions/47307873/read-entire-database-with-sqlalchemy-and-dump-as-json
    engine = db.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    ret = { }
    for tbl in metadata.sorted_tables:
        ret[tbl.name] = [dict(r) for r in engine.execute(tbl.select())]
    return ret

@click.command("dump-db")
@with_appcontext
def dump_db_command():
    db_content = get_all_db_content()

    click.echo(json.dumps(db_content, indent=2, default=str))
    # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

##__________________________________________________________________||
