"""DB operations

"""
import os
import datetime
import csv

from sqlalchemy import MetaData
import sqlalchemy

from .sa import sa
from .conn import get_db_connection

##__________________________________________________________________||
def init_db():

    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)

    if metadata.tables:
        tbl_names = metadata.tables.keys()
        # ['maps', 'beams']

        tbl_names = ', '.join(['"{}"'.format(t) for t in tbl_names])
        # '"beams", "maps"'

        msg = "Dropped all tables: {}".format(tbl_names)

        metadata.drop_all(bind=engine)
        print(msg)

    if not sa.Model.metadata.tables:
        msg = "No tables to be created are found!"
        print(msg)
        return

    tbl_names = sa.Model.metadata.tables.keys()
    # ['maps', 'beams']

    tbl_names = ', '.join(['"{}"'.format(t) for t in tbl_names])
    # '"beams", "maps"'

    msg = "Created tables: {}".format(tbl_names)

    sa.Model.metadata.create_all(engine)

    print(msg)

##__________________________________________________________________||
def get_all_db_content():
    # https://stackoverflow.com/questions/47307873/read-entire-database-with-sqlalchemy-and-dump-as-json
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    ret = { }
    for tbl in metadata.sorted_tables:
        ret[tbl.name] = [dict(r) for r in engine.execute(tbl.select())]
    return ret

##__________________________________________________________________||
def import_csv(csvdir):
    metadata = MetaData()
    metadata.reflect(bind=sa.engine)
    for tbl in metadata.sorted_tables:
        csv_filename = '{}.csv'.format(tbl.name)
        csv_path = os.path.join(csvdir, csv_filename)
        if os.path.exists(csv_path):
            import_csv_(tbl, csv_path)
            message = 'imported to "{}" from {}'.format(tbl.name, csv_path)
        else:
            message = 'skipped "{}". file not found: {}'.format(tbl.name, csv_path)
        print(message)

def import_csv_(tbl, csv_path):
    with open(csv_path, 'r') as f:
        rows = list(csv.reader(f))
    fields = rows[0]
    rows = rows[1:]
    data = [{f: convert_type(e, tbl.columns[f].type) for f, e in zip(fields, r)} for r in rows]
    ins = tbl.insert()
    connection = get_db_connection()
    connection.execute(ins, data)

def convert_type(str_, type_):
    if isinstance(type_, sqlalchemy.sql.sqltypes.DATE):
        if str_:
            return datetime.datetime.strptime(str_, "%Y-%m-%d").date()
        return None
    return str_

##__________________________________________________________________||
