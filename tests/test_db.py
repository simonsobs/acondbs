import pytest
import unittest.mock as mock

import sqlalchemy

from acondbs.db import get_db_connection

##__________________________________________________________________||
def test_get_close_db(app):
    with app.app_context():
        db = get_db_connection()
        assert db is get_db_connection()

    with pytest.raises(sqlalchemy.exc.StatementError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)

##__________________________________________________________________||
@pytest.fixture()
def mock_init_db(monkeypatch):
    ret = mock.Mock()
    monkeypatch.setattr("acondbs.db.init_db", ret)
    return ret

##__________________________________________________________________||
def test_init_db_command(runner, mock_init_db):
    result = runner.invoke(args=["init-db"])
    assert [mock.call()] == mock_init_db.call_args_list
    assert "Initialized" in result.output

##__________________________________________________________________||
