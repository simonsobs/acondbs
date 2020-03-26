"""DB

This module is similar to `db.py` in `falskr`, an example application
described in the flask tutorial.

 The flask tutorial: https://flask.palletsprojects.com/en/1.1.x/tutorial/

 db.py in flaskr: https://github.com/pallets/flask/blob/1.1.1/examples/tutorial/flaskr/db.py

"""

from flask import g
from flask_sqlalchemy import SQLAlchemy


##__________________________________________________________________||
sa = SQLAlchemy()
"""the instance of SQLAlchemy

"""
##__________________________________________________________________||
def get_db_connection():
    """returns the DB connection

    This function returns the `connection` of SQLAlchemy:
    https://docs.sqlalchemy.org/en/13/core/connections.html

    This function is similar to `get_db()` in `falskr`.

    """
    if 'db_connection' not in g:
        g.db_connection = sa.engine.connect()
    return g.db_connection

##__________________________________________________________________||
def close_db_connection(e=None):
    """closes the DB connection

    This function is registered to be called when the application ends.

    This function is similar to `close_db()` in `falskr`.
    """
    conn = g.pop('db_connection', None)
    if conn is not None:
        conn.close()

##__________________________________________________________________||
def init_app(app):
    """initializes the application object

    This function is called by `create_app()`
    """
    sa.init_app(app)

    from .cmds import init_db_command, dump_db_command, import_csv_command
    app.cli.add_command(init_db_command)
    app.cli.add_command(dump_db_command)
    app.cli.add_command(import_csv_command)
    app.teardown_appcontext(close_db_connection)

##__________________________________________________________________||
