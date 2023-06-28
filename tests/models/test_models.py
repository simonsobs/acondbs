from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from acondbs.db.sa import sa


def test_table_names(app_empty: Flask, snapshot: PyTestSnapshotTest) -> None:
    '''test the table names'''
    table_names = list(sa.Model.metadata.tables.keys())  # type: ignore
    snapshot.assert_match(table_names)
