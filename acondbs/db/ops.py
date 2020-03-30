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
def define_tables():
    """defines tables in the DB

    This function defines tables in the DB after dropping all existing
    tables.

    This function needs to be called within the application context of
    Flask.

    """

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
    return export_db_to_dict_of_dict_list()

##__________________________________________________________________||
def get_all_table_names():
    """returns the names of all tables in the DB.

    Returns
    -------
    list of str
        the names of all tables in the DB

    """
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return [tbl.name for tbl in metadata.sorted_tables]

def export_db_to_dict_of_dict_list():
    """exports the DB to a dict of table names and lists of dicts for each row

    Returns
    -------
    dict
        dict with one entry for each table: the table name as the key
        and the value lists of dicts: one dict for each row: field
        names as the keys and contents as the values. e.g.,

            {"tblA": [
                {'fieldA': 1001, 'fieldB': 'abc'},
                {'fieldA': 1002, 'fieldB': 'xyz'}
            ]}

    """
    tbl_names = get_all_table_names()
    ret = {n: export_table_to_dict_list(n) for n in tbl_names}
    return ret

def export_table_to_dict_list(tbl_name):
    """exports the table to a list of dicts

    Parameters
    ----------
    tbl_name : str
        the table name

    Returns
    -------
    list of dict
        the list of dicts: one dict for each row: field names as the
        keys and contents as the values. e.g.:

            [
                {'fieldA': 1001, 'fieldB': 'abc'},
                {'fieldA': 1002, 'fieldB': 'xyz'}
            ]

    """
    result_proxy = get_resultproxy_of_select_all_rows(tbl_name)
    return [dict(r) for r in result_proxy]

def get_resultproxy_of_select_all_rows(tbl_name):
    """returns ResultProxy with all rows of the table

    Parameters
    ----------
    tbl_name : str
        the table name

    Returns
    -------
    ResultProxy
        ResultProxy of SQLAlchemy with the result of query selecting
        all rows of the table.
        https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.ResultProxy

    """
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tbl = metadata.tables[tbl_name]
    return engine.execute(tbl.select())

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
