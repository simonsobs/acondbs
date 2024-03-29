import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest
from sqlalchemy import MetaData

from acondbs import create_app
from acondbs.db.ops import define_tables
from acondbs.db.sa import sa


@pytest.fixture
def app_with_empty_db() -> Flask:
    database_uri = 'sqlite:///:memory:'
    app = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    return app


def test_define_tables_start_with_empty_db(
    app_with_empty_db: Flask, snapshot: PyTestSnapshotTest
) -> None:
    '''test define_tables()

    This function tests if tables will be defined starting from new db without
    any tables.

    '''

    app = app_with_empty_db

    # confirm tables are not defined initially
    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=sa.engine)
        assert not metadata.tables

    with app.app_context():
        define_tables()

    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=sa.engine)
        snapshot.assert_match(metadata.tables)


def test_define_tables_start_with_nonempty_db(
    app: Flask, snapshot: PyTestSnapshotTest
) -> None:
    '''test define_tables()

    This function tests if tables will be redefined starting from db
    with tables with entries.

    '''

    # confirm tables are defined initially and not empty
    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=sa.engine)
        assert metadata.tables
        total_nentries = sum(
            [
                len([r for r in sa.session.execute(tbl.select())])
                for tbl in metadata.sorted_tables
            ]
        )
        assert total_nentries > 0

    with app.app_context():
        define_tables()

    # confirm tables are defined and all empty
    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=sa.engine)
        snapshot.assert_match(metadata.tables)
        total_nentries = sum(
            [
                len([r for r in sa.session.execute(tbl.select())])
                for tbl in metadata.sorted_tables
            ]
        )
        assert total_nentries == 0
