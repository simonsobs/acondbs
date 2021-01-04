from pathlib import Path
import threading
import shutil
import datetime

import pytest
import unittest.mock as mock

from acondbs import create_app

from acondbs.db.ops import define_tables, import_tables_from_csv_files

##__________________________________________________________________||
from .constants import SAMPLE_DIR

##__________________________________________________________________||
@pytest.fixture(scope="session")
def create_db_with_csv_files():
    """create a test DB, load data from CSV files

    """
    config_path = Path(SAMPLE_DIR, 'config.py')
    csvdir = Path(SAMPLE_DIR, 'csv')
    app = create_app(config_path=config_path)
    with app.app_context():
        define_tables()
        import_tables_from_csv_files(csvdir)
    yield
    database_path = Path(SAMPLE_DIR, 'product.sqlite3')
    database_path.unlink()

##__________________________________________________________________||
@pytest.fixture
def database_uri(create_db_with_csv_files, tmpdir_factory):
    """the database URI for a temporarily copy of the test data

    The fixture copies the test data `product.sqlite3` to a
    temporarily folder and returns the URI for the copy.

    """
    org_database_path = Path(SAMPLE_DIR, 'product.sqlite3')
    tmpdir = str(tmpdir_factory.mktemp('instance'))
    tmp_database_path = Path(tmpdir, 'product.sqlite3')
    shutil.copy2(org_database_path, tmp_database_path)
    ret = 'sqlite:///{}'.format(tmp_database_path)
    yield ret

##__________________________________________________________________||
@pytest.fixture
def app(database_uri):
    """a test Flask application

    The `app` is an instance of `Flask`. Its API is described in the
    Flask documentation at
    https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask

    The `app` is initialized for the SQLAlchemy DB with URI at
    `database_uri`.

    Yields
    ------
    Flask

    """
    config_path = Path(SAMPLE_DIR, 'config.py')
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    yield app

##__________________________________________________________________||
@pytest.fixture
def client(app):
    """a test client of the Flask application

    The test client, an instance of `FlaskClient`, can emulate HTTP
    requests, e.g, GET, POST. For example::

        response = client.get('/')

    The response object (`Response`) can be examined for tests

    More in the Flask documentation:
    `FlaskClient`: https://flask.palletsprojects.com/en/1.1.x/api/#test-client
    `Response`: https://flask.palletsprojects.com/en/1.1.x/api/#response-objects
    `test_client()`: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client


    Yields
    ------
    FlaskClient

    """
    yield app.test_client()

##__________________________________________________________________||
@pytest.fixture
def runner(app):
    """a test CLI runner of the Flask application

    The runner (`FlaskCliRunner`) is used to test custom click
    commands.

    More in the Flask documentation:
    `FlaskCliRunner`: https://flask.palletsprojects.com/en/1.1.x/api/#test-cli-runner
    `Result`: https://click.palletsprojects.com/en/7.x/api/#click.testing.Result
    `test_cli_runner()`: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_cli_runner

    Yields
    ------
    FlaskCliRunner

    """
    yield app.test_cli_runner()

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def db_backup_global_variables(monkeypatch):
    from acondbs.db import backup
    monkeypatch.setattr(backup, '_lock', threading.Lock())
    monkeypatch.setattr(backup, '_capped_backup_func', None)
    yield
    backup.end_backup_thread()

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_request_backup_db(monkeypatch):
    """mock request_backup_db() so that backups won't be actually taken in tests
    """
    y = mock.Mock()
    monkeypatch.setattr("acondbs.schema.product.product.request_backup_db", y)
    monkeypatch.setattr("acondbs.schema.product.product_file_path.request_backup_db", y)
    monkeypatch.setattr("acondbs.schema.product.product_type.request_backup_db", y)
    monkeypatch.setattr("acondbs.schema.product.product_relation_type.request_backup_db", y)
    monkeypatch.setattr("acondbs.schema.product.product_relation.request_backup_db", y)
    monkeypatch.setattr("acondbs.schema.github.mutation.request_backup_db", y)
    yield y

##__________________________________________________________________||
@pytest.fixture(autouse=True)
def mock_datetime(monkeypatch):
    """mock datetime so that datetime.date.today() and datetime.datetime.now()
    always returns the same value

    """
    y = mock.Mock(wraps=datetime)
    y.date.today.return_value = datetime.date(2020, 5, 4)
    y.datetime.now.return_value = datetime.datetime(2021, 1, 4, 14, 32, 20)
    monkeypatch.setattr("acondbs.schema.product.product.datetime", y)
    monkeypatch.setattr("acondbs.models.github.github_token.datetime", y)
    yield y

##__________________________________________________________________||
