from pathlib import Path

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from acondbs import create_app
from acondbs.db.ops import (
    define_tables,
    export_db_to_csv_files,
    export_db_to_dict_of_dict_list,
    import_tables_from_csv_files,
)

from ...constants import SAMPLE_DIR


@pytest.fixture
def app() -> Flask:
    config_path = Path(SAMPLE_DIR, 'config.py')
    database_uri = 'sqlite:///:memory:'
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    csvdir = Path(SAMPLE_DIR, 'csv')
    with app.app_context():
        define_tables()
        import_tables_from_csv_files(csvdir)
    return app


def test_export_db_to_csv_files(
    app: Flask, tmp_path_factory: pytest.TempPathFactory, snapshot: PyTestSnapshotTest
) -> None:
    outdir = tmp_path_factory.mktemp('csv')

    with app.app_context():
        export_db_to_csv_files(outdir)

    with app.app_context():
        define_tables()
        import_tables_from_csv_files(outdir)
        snapshot.assert_match(export_db_to_dict_of_dict_list())
