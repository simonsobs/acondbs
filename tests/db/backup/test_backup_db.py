import unittest.mock as mock
import warnings

import pytest

from acondbs.db.backup import backup_db


@pytest.fixture()
def mock_backup_db_to_github(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import backup

    y = mock.Mock()
    monkeypatch.setattr(backup, 'backup_db_to_github', y)
    return y


@pytest.fixture()
def mock_backup_db_as_csv_to_github(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import backup

    y = mock.Mock()
    monkeypatch.setattr(backup, 'backup_db_as_csv_to_github', y)
    return y


def test_backup_db(
    mock_backup_db_to_github: mock.Mock, mock_backup_db_as_csv_to_github: mock.Mock
) -> None:
    backup_db()
    mock_backup_db_to_github.assert_called_once()
    mock_backup_db_as_csv_to_github.assert_called_once()


def test_exceptions(
    mock_backup_db_to_github: mock.Mock, mock_backup_db_as_csv_to_github: mock.Mock
) -> None:
    mock_backup_db_to_github.side_effect = Exception()
    mock_backup_db_as_csv_to_github.side_effect = Exception()
    with warnings.catch_warnings(record=True) as w:
        backup_db()
    assert len(w) == 2
    mock_backup_db_to_github.assert_called_once()
    mock_backup_db_as_csv_to_github.assert_called_once()
