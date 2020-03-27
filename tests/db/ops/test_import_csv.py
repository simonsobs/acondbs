import os
import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables, import_csv, get_all_db_content

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
def test_import_csv(app, snapshot):
    csvdir = os.path.join(SAMPLE_DIR, 'csv')
    with app.app_context():
        import_csv(csvdir)
    with app.app_context():
        snapshot.assert_match(get_all_db_content())

##__________________________________________________________________||
