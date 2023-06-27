import datetime
import shutil
import threading
import unittest.mock as mock
from pathlib import Path
from typing import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner

from acondbs import create_app
from acondbs.db.ops import define_tables, import_tables_from_csv_files

from .constants import SAMPLE_DIR


@pytest.fixture(scope='session')
def create_db_with_csv_files() -> Iterator[None]:
    '''create a test DB, load data from CSV files'''
    config_path = SAMPLE_DIR / 'config.py'
    csvdir = SAMPLE_DIR / 'csv'
    app = create_app(config_path=config_path)
    with app.app_context():
        define_tables()
        import_tables_from_csv_files(csvdir)
    yield
    database_path = SAMPLE_DIR / 'product.sqlite3'
    database_path.unlink()


@pytest.fixture
def database_uri(
    create_db_with_csv_files: None, tmp_path_factory: pytest.TempPathFactory
) -> str:
    '''The database URI for a temporarily copy of the test data

    The fixture copies the test data `product.sqlite3` to a
    temporarily folder and returns the URI for the copy.

    '''
    del create_db_with_csv_files
    org_database_path = SAMPLE_DIR / 'product.sqlite3'
    tmpdir = tmp_path_factory.mktemp('instance')
    tmp_database_path = tmpdir / 'product.sqlite3'
    shutil.copy2(org_database_path, tmp_database_path)
    ret = f'sqlite:///{str(tmp_database_path)}'
    return ret


@pytest.fixture
def app(database_uri: str) -> Flask:
    '''a test Flask application

    The `app` is an instance of `Flask`. Its API is described in the
    Flask documentation at
    https://flask.palletsprojects.com/en/2.3.x/api/#flask.Flask

    The `app` is initialized for the SQLAlchemy DB with URI at
    `database_uri`.

    '''
    config_path = Path(SAMPLE_DIR, 'config.py')
    app = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    return app


@pytest.fixture
def client(app: Flask) -> Iterator[FlaskClient]:
    '''a test client of the Flask application

    The test client, an instance of `FlaskClient`, can emulate HTTP
    requests, e.g, GET, POST. For example::

        response = client.get('/')

    The response object (`Response`) can be examined for tests

    More in the Flask documentation:
    `FlaskClient`: https://flask.palletsprojects.com/en/2.3.x/api/#test-client
    `Response`: https://flask.palletsprojects.com/en/2.3.x/api/#response-objects
    `test_client()`: https://flask.palletsprojects.com/en/2.3.x/api/#flask.Flask.test_client


    '''
    with app.test_client() as y:
        yield y


@pytest.fixture
def runner(app: Flask) -> FlaskCliRunner:
    '''a test CLI runner of the Flask application

    The runner (`FlaskCliRunner`) is used to test custom click
    commands.

    More in the Flask documentation:
    `FlaskCliRunner`: https://flask.palletsprojects.com/en/2.3.x/api/#test-cli-runner
    `Result`: https://click.palletsprojects.com/en/8.1.x/api/#click.testing.Result
    `test_cli_runner()`: https://flask.palletsprojects.com/en/2.3.x/api/#flask.Flask.test_cli_runner

    '''
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def db_backup_global_variables(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    from acondbs.db import backup

    monkeypatch.setattr(backup, '_lock', threading.Lock())
    monkeypatch.setattr(backup, '_capped_backup_func', None)
    yield
    backup.end_backup_thread()


@pytest.fixture(autouse=True)
def mock_request_backup_db(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    '''mock request_backup_db() so that backups won't be actually taken in tests'''

    targets = [
        'acondbs.schema.github.mutation.request_backup_db',
        'acondbs.ops.misc.request_backup_db',
    ]
    y = mock.Mock()
    for t in targets:
        monkeypatch.setattr(t, y)
    return y


@pytest.fixture(autouse=True)
def mock_datetime(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    '''mock datetime so that datetime.date.today() and datetime.datetime.now()
    always returns the same value

    '''

    targets = [
        'acondbs.models.github.github_token.datetime',
        'acondbs.models.product.product.datetime',
        'acondbs.models.misc.log.datetime',
        'acondbs.ops.product.datetime',
    ]

    y = mock.Mock(wraps=datetime)
    y.date.today.return_value = datetime.date(2020, 5, 4)
    y.datetime.now.return_value = datetime.datetime(2021, 1, 4, 14, 32, 20)
    for t in targets:
        monkeypatch.setattr(t, y)
    return y
