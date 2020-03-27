import os
import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables, import_csv, get_all_db_content

##__________________________________________________________________||
_THISDIR = os.path.dirname(os.path.realpath(__file__))
_TESTDIRTOP = os.path.dirname(os.path.dirname(_THISDIR))
_SAMPLEDIR = os.path.join(_TESTDIRTOP, 'sample')
print(_TESTDIRTOP)

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
    csvdir = os.path.join(_SAMPLEDIR, 'csv')
    with app.app_context():
        import_csv(csvdir)
    with app.app_context():
        snapshot.assert_match(get_all_db_content())

##__________________________________________________________________||
