import unittest.mock as mock

import pytest
from flask.testing import FlaskCliRunner

from ..constants import SAMPLE_DIR


@pytest.fixture()
def mock_define_tables(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import cmds

    ret = mock.Mock()
    monkeypatch.setattr(cmds, 'define_tables', ret)
    return ret


def test_init_db_command(runner: FlaskCliRunner, mock_define_tables: mock.Mock) -> None:
    '''test command init-db'''
    result = runner.invoke(args=['init-db'])
    assert [mock.call()] == mock_define_tables.call_args_list
    assert 'Initialized' in result.output


def test_dump_db_command(runner: FlaskCliRunner) -> None:
    '''test command dump-db'''
    result = runner.invoke(args=['dump-db'])
    assert 0 == result.exit_code
    assert 1800 < len(result.output)


@pytest.fixture()
def mock_import_tables_from_csv_files(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import cmds

    ret = mock.Mock()
    monkeypatch.setattr(cmds, 'import_tables_from_csv_files', ret)
    return ret


def test_import_csv_command(
    runner: FlaskCliRunner, mock_import_tables_from_csv_files: mock.Mock
) -> None:
    '''test command import-csv'''

    csvdir = SAMPLE_DIR / 'csv'
    # needs to give an existing path to `import-csv` as `click.Path()`
    # checks the check the existence.

    result = runner.invoke(args=['import-csv', str(csvdir)])
    assert 0 == result.exit_code
    assert [mock.call(str(csvdir))] == mock_import_tables_from_csv_files.call_args_list


@pytest.fixture()
def mock_export_db_to_csv_files(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import cmds

    ret = mock.Mock()
    monkeypatch.setattr(cmds, 'export_db_to_csv_files', ret)
    return ret


def test_export_csv_command(
    runner: FlaskCliRunner,
    tmp_path_factory: pytest.TempPathFactory,
    mock_export_db_to_csv_files: mock.Mock,
) -> None:
    '''test command export-csv'''

    tmpdir = tmp_path_factory.mktemp('csv_out')
    csvdir = tmpdir / 'csv'

    result = runner.invoke(args=['export-csv', str(csvdir)])
    assert 0 == result.exit_code
    assert [mock.call(str(csvdir))] == mock_export_db_to_csv_files.call_args_list
