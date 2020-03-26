import pytest
import unittest.mock as mock

import sqlalchemy

from acondbs.db.db import get_db_connection
from acondbs.db.ops import init_db

##__________________________________________________________________||
def test_get_close_db_connection(app):
    with app.app_context():
        conn = get_db_connection()
        assert conn is get_db_connection()

    with pytest.raises(sqlalchemy.exc.StatementError) as e:
        conn.execute("SELECT 1")

    assert "closed" in str(e.value)

##__________________________________________________________________||
def test_init_db(app):
    with app.app_context():
        init_db()

##__________________________________________________________________||
@pytest.fixture()
def mock_init_db(monkeypatch):
    ret = mock.Mock()
    monkeypatch.setattr("acondbs.db.cmds.init_db", ret)
    return ret

def test_init_db_command(runner, mock_init_db):
    result = runner.invoke(args=["init-db"])
    assert [mock.call()] == mock_init_db.call_args_list
    assert "Initialized" in result.output

##__________________________________________________________________||
def test_dump_db_command(runner):
    result = runner.invoke(args=["dump-db"])
    assert 0 == result.exit_code
    assert 1800 < len(result.output)

##__________________________________________________________________||
@pytest.fixture()
def mock_import_csv(monkeypatch):
    ret = mock.Mock()
    monkeypatch.setattr("acondbs.db.cmds.import_csv", ret)
    return ret

def test_import_csv_command(runner, mock_import_csv):
    result = runner.invoke(args=["import-csv", "../../csv"])
    assert 0 == result.exit_code
    assert [mock.call('../../csv')] == mock_import_csv.call_args_list

##__________________________________________________________________||
