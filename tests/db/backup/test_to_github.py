import unittest.mock as mock
import warnings
from pathlib import Path

import pytest
from flask import Flask

from acondbs.db.backup import backup_db_to_github


@pytest.fixture()
def mock_backup_db_to_github_(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import backup

    y = mock.Mock()
    monkeypatch.setattr(backup, 'backup_db_to_github_', y)
    return y


@pytest.fixture()
def mock_lock_path(
    app: Flask,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path_factory: pytest.TempPathFactory,
) -> Path:
    folder = tmp_path_factory.mktemp('backup')
    y = folder / 'lock'
    monkeypatch.setitem(app.config, 'ACONDBS_DB_BACKUP_LOCK', str(y))
    monkeypatch.setitem(app.config, 'ACONDBS_DB_BACKUP_LOCK_TIMEOUT', 0.01)
    return y


def test_backup_db_to_github(
    app: Flask, mock_lock_path: Path, mock_backup_db_to_github_: mock.Mock
) -> None:
    del mock_lock_path
    with app.app_context():
        repo_path = app.config['ACONDBS_DB_FOLDER']
        backup_db_to_github()
    assert [mock.call(repo_path)] == mock_backup_db_to_github_.call_args_list


def test_backup_db_locked(
    app: Flask, mock_lock_path: Path, mock_backup_db_to_github_: mock.Mock
) -> None:
    mock_lock_path.touch()
    with app.app_context():
        with warnings.catch_warnings(record=True) as w:
            backup_db_to_github()
    assert [] == mock_backup_db_to_github_.call_args_list
    assert len(w) == 1
