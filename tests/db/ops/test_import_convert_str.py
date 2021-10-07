import csv
from io import StringIO

import datetime

from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EncryptedType

import pytest

from acondbs import create_app
from acondbs.db.ops import convert_data_type_for_insert


##__________________________________________________________________||
sa = SQLAlchemy()


class SampleTable(sa.Model):
    __tablename__ = "sample_table"
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
    encrypted = sa.Column(EncryptedType(sa.Text(), "8b5d3d25b3e5"))


##__________________________________________________________________||
@pytest.fixture
def app_with_empty_db():
    database_uri = "sqlite:///:memory:"
    app = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    yield app


@pytest.fixture
def app_with_empty_tables(app_with_empty_db):
    app = app_with_empty_db

    # define tables
    with app.app_context():
        engine = sa.engine
        metadata = MetaData()
        metadata.reflect(bind=engine)
        sa.Model.metadata.create_all(engine)
    yield app


@pytest.fixture
def app(app_with_empty_tables):
    app = app_with_empty_tables

    # enter data
    with app.app_context():
        row = SampleTable(
            text="abcde",
            unicode_text="絵文字😀 😃 😄 😁 😆",
            boolean=True,
            integer=512,
            float=2.34556234,
            date=datetime.datetime(2021, 10, 7),
            date_time=datetime.datetime(2021, 10, 7, 15, 4, 20),
            time=datetime.time(15, 4, 20),
            encrypted="secret string"
        )
        sa.session.add(row)
        sa.session.commit()

    yield app


##__________________________________________________________________||
def test_convert(app):
    """test convert_data_type_for_insert()"""
    tbl_name = "sample_table"

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

        engine = sa.engine
        metadata = MetaData()
        metadata.reflect(bind=engine)
        tbl = metadata.tables[tbl_name]

        rows = list(csv.reader(StringIO(csv_str)))
        fields = rows[0]
        rows = rows[1:]

        data = [
            {
                f: convert_data_type_for_insert(e, tbl.columns[f].type)
                for f, e in zip(fields, r)
            }
            for r in rows
        ]

        ins = tbl.insert()
        connection = sa.engine.connect()
        connection.execute(ins, data)

    # assert
    with app.app_context():
        row = SampleTable.query.one()
        assert row.text == "abcde"
        assert row.unicode_text == "絵文字😀 😃 😄 😁 😆"
        assert row.boolean is True
        assert row.float == 2.34556234
        assert row.date == datetime.date(2021, 10, 7)
        assert row.date_time == datetime.datetime(2021, 10, 7, 15, 4, 20)
        assert row.time == datetime.time(15, 4, 20)
        assert row.encrypted == "secret string"


def _export_tbl_to_csv(tbl_name):
    engine = sa.engine
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tbl = metadata.tables[tbl_name]
    result_proxy = engine.execute(tbl.select())
    b = StringIO()
    csv_writer = csv.writer(b, lineterminator="\n")
    csv_writer.writerow(result_proxy.keys())
    csv_writer.writerows(result_proxy)
    ret = b.getvalue()
    b.close()
    return ret


##__________________________________________________________________||
