import os

import pytest
import unittest.mock as mock

from ..constants import SAMPLE_DIR

##__________________________________________________________________||
@pytest.fixture()
def mock_define_tables(monkeypatch):
    ret = mock.Mock()
    monkeypatch.setattr("acondbs.db.cmds.define_tables", ret)
    return ret

def test_init_db_command(runner, mock_define_tables):
    result = runner.invoke(args=["init-db"])
    assert [mock.call()] == mock_define_tables.call_args_list
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
    csvdir = os.path.join(SAMPLE_DIR, 'csv')
    result = runner.invoke(args=["import-csv", csvdir])
    assert 0 == result.exit_code
    assert [mock.call(csvdir)] == mock_import_csv.call_args_list

##__________________________________________________________________||
