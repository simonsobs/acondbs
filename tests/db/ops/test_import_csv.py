from pathlib import Path
import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables
from acondbs.db.ops import import_tables_from_csv_files
from acondbs.db.ops import export_db_to_dict_of_dict_list
from acondbs.db.ops import export_db_to_csv_files

from ...constants import SAMPLE_DIR

##__________________________________________________________________||
@pytest.fixture
def app():
    database_uri ="sqlite:///:memory:"
    app = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with app.app_context():
        define_tables()
    yield app


##__________________________________________________________________||
def test_import_tables_from_csv_files(app, snapshot):
    csvdir = Path(SAMPLE_DIR, 'csv')
    with app.app_context():
        import_tables_from_csv_files(csvdir)
    with app.app_context():
        snapshot.assert_match(export_db_to_dict_of_dict_list())

##__________________________________________________________________||
def test_import_empty_tables_from_csv_files(app, tmpdir_factory, snapshot):
    csvdir = str(tmpdir_factory.mktemp('csv'))

    with app.app_context():
        export_db_to_csv_files(csvdir)

    with app.app_context():
        import_tables_from_csv_files(csvdir)

##__________________________________________________________________||
