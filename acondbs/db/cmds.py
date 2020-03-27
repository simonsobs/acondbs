"""Commands (click)

"""
from flask.cli import with_appcontext
import click

import json

from .ops import define_tables, get_all_db_content, import_csv

##__________________________________________________________________||
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    define_tables()
    click.echo("Initialized the database.")

##__________________________________________________________________||
@click.command("dump-db")
@with_appcontext
def dump_db_command():
    """Dump the DB contents

    """
    db_content = get_all_db_content()

    click.echo(json.dumps(db_content, indent=2, default=str))
    # https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable

##__________________________________________________________________||
@click.command("import-csv")
@click.argument("csvdir", type=click.Path(exists=True))
@with_appcontext
def import_csv_command(csvdir):
    """Import tables from CSV files in CSVDIR into the DB.

    """
    import_csv(csvdir)

##__________________________________________________________________||
