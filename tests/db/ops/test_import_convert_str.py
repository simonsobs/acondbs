import csv
import datetime
from io import StringIO
from typing import Any

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_utils import EncryptedType

# from acondbs import create_app
from acondbs.db.ops import convert_data_type_for_insert

sa = SQLAlchemy()


class SampleTable(sa.Model):  # type: ignore
    __tablename__ = 'sample_table'
    id_ = sa.Column(sa.Integer(), primary_key=True)

    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types
    text = sa.Column(sa.Text())
    unicode_text = sa.Column(sa.UnicodeText())
    boolean = sa.Column(sa.Boolean())
    integer = sa.Column(sa.Integer())
    float = sa.Column(sa.Float())
    date = sa.Column(sa.Date())
    date_time = sa.Column(sa.DateTime())
    time = sa.Column(sa.Time())
    encrypted = sa.Column(EncryptedType(sa.Text(), '8b5d3d25b3e5'))


@pytest.fixture
def app_with_empty_db() -> Flask:
    database_uri = 'sqlite:///:memory:'
    # app = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(**{'SQLALCHEMY_DATABASE_URI': database_uri})  # type: ignore
    sa.init_app(app)  # type: ignore
    return app


@pytest.fixture
def app_with_empty_tables(app_with_empty_db: Flask) -> Flask:
    app = app_with_empty_db

    # define tables
    with app.app_context():
        engine = sa.engine
        metadata = MetaData()
        metadata.reflect(bind=engine)
        metadata.drop_all(bind=engine)
        sa.Model.metadata.create_all(engine)  # type: ignore
    return app


params = [
    pytest.param(
        dict(
            text='abcde',
            unicode_text='絵文字😀 😃 😄 😁 😆',
            boolean=False,
            integer=512,
            float=2.34556234,
            date=datetime.date(2021, 10, 7),
            date_time=datetime.datetime(2021, 10, 7, 15, 4, 20),
            time=datetime.time(15, 4, 20),
            encrypted='secret string',
        ),
        id='one',
    ),
    pytest.param(
        dict(
            boolean=True,
        ),
        id='bool-true',
    ),
    pytest.param(
        dict(
            text='',
            unicode_text='',
            boolean=None,
            integer=None,
            float=None,
            date=None,
            date_time=None,
            time=None,
            encrypted=None,
        ),
        id='none',
    ),
]


@pytest.mark.parametrize('data', params)
def test_convert(app_with_empty_tables: Flask, data: dict[str, Any]) -> None:
    '''test convert_data_type_for_insert()'''
    app = app_with_empty_tables

    tbl_name = 'sample_table'

    expected = list(data.items())  # e.g., [('text', 'abcde'), ...]
    fields = list(data.keys())  # .e.,g ['text', 'unicode_text', ...]

    # delete all rows from the table
    # The table is not empty! Not clear why!
    with app.app_context():
        SampleTable.query.delete()
        sa.session.commit()

    # enter data
    with app.app_context():
        row = SampleTable(**data)
        sa.session.add(row)
        sa.session.commit()

    # assert the data are committed as they entered
    with app.app_context():
        row = SampleTable.query.one()
        actual = [(f, getattr(row, f)) for f in fields]
        assert actual == expected

    # export to csv as string
    with app.app_context():
        csv_str = _export_tbl_to_csv(tbl_name)

        # empty the table
        SampleTable.query.delete()
        sa.session.commit()

    # import from the csv
    with app.app_context():
        # confirm the table is empty
        assert SampleTable.query.count() == 0

        _import_tbl_from_csv(tbl_name, csv_str)
        sa.session.commit()

    # assert
    with app.app_context():
        row = SampleTable.query.one()
        actual = [(f, getattr(row, f)) for f in fields]
        assert actual == expected


def _export_tbl_to_csv(tbl_name: str) -> str:
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tbl = metadata.tables[tbl_name]
    result_proxy = sa.session.execute(tbl.select())
    b = StringIO()
    csv_writer = csv.writer(b, lineterminator='\n')
    csv_writer.writerow(result_proxy.keys())
    csv_writer.writerows(result_proxy)
    ret = b.getvalue()
    b.close()
    return ret


def _import_tbl_from_csv(tbl_name: str, csv_str: str) -> None:
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tbl = metadata.tables[tbl_name]

    rows = list(csv.reader(StringIO(csv_str)))
    fields = rows[0]
    rows = rows[1:]

    field_types = [tbl.columns[f].type for f in fields]

    data = [
        {
            f: convert_data_type_for_insert(e, t)
            for f, t, e in zip(fields, field_types, r)
        }
        for r in rows
    ]

    ins = tbl.insert()
    sa.session.execute(ins, data)
