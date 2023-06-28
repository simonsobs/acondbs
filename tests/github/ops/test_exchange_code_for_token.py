import unittest.mock as mock

import pytest
from flask import Flask
from snapshottest.pytest import PyTestSnapshotTest

from acondbs.github.ops import exchange_code_for_token


@pytest.fixture(autouse=True)
def mock_call(monkeypatch: pytest.MonkeyPatch) -> mock.Mock:
    from acondbs.github import ops

    y = mock.Mock()
    monkeypatch.setattr(ops, 'call', y)
    return y


def test_call(app: Flask, snapshot: PyTestSnapshotTest, mock_call: mock.Mock) -> None:
    code = 'kp5b8653'
    return_value = {'access_token': 'wuk5phc8', 'token_type': 'bearer', 'scope': 'user'}
    mock_call.exchange_code_for_token.return_value = dict(return_value)
    with app.app_context():
        ret = exchange_code_for_token(code)
    assert ret == return_value
    snapshot.assert_match(mock_call.exchange_code_for_token.call_args_list)
