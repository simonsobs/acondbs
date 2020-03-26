"""Commands (click)

"""
from flask.cli import with_appcontext
import click

import json

from .ops import init_db, get_all_db_content, import_csv

##__________________________________________________________________||
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

##__________________________________________________________________||
@click.command("dump-db")
@with_appcontext
def dump_db_command():
    db_content = get_all_db_content()

    click.echo(json.dumps(db_content, indent=2, default=str))
    # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

##__________________________________________________________________||
@click.command("import-csv")
@click.argument("csvdir")
@with_appcontext
def import_csv_command(csvdir):
    import_csv(csvdir)

##__________________________________________________________________||
