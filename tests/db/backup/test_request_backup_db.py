import unittest.mock as mock
from flask import Flask

import pytest

from acondbs.db.backup import request_backup_db, run_flask_backup_db


@pytest.fixture()
def mock_cap_exec_rate(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.db import backup

    y = mock.Mock()
    monkeypatch.setattr(backup, 'cap_exec_rate', y)
    return y


def test_request_backup_db(app: Flask, mock_cap_exec_rate: mock.Mock) -> None:
    with app.app_context():
        pause = app.config['ACONDBS_DB_BACKUP_PAUSE']

    nrequests = 3
    with app.app_context():
        for i in range(nrequests):
            request_backup_db()

    assert 1 == mock_cap_exec_rate.call_count
    assert [
        mock.call(func=run_flask_backup_db, pause_time=pause, daemon=True)
    ] == mock_cap_exec_rate.call_args_list

    assert nrequests == mock_cap_exec_rate().call_count
