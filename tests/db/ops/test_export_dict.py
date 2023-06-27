from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from acondbs.db.ops import export_db_to_dict_of_dict_list


def test_export_db_to_dict_of_dict_list(
    app: Flask, snapshot: PyTestSnapshotTest
) -> None:
    '''test export_db_to_dict_of_dict_list()'''

    with app.app_context():
        snapshot.assert_match(export_db_to_dict_of_dict_list())
