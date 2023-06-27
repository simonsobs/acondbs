from pathlib import Path
from typing import Any

import pytest

from acondbs import create_app

TEST_CONFIG_DICT_DEFAULT = dict(
    TEST_CONFIG_A='abc',
    TEST_CONFIG_B=123,
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

TEST_CONFIG_FILE_CONTENT = '''\
TEST_CONFIG_B = 456
TEST_CONFIG_C = False
'''


@pytest.fixture(autouse=True)
def mock_default_config_dict(monkeypatch: pytest.MonkeyPatch) -> dict[str, Any]:
    ret = TEST_CONFIG_DICT_DEFAULT
    monkeypatch.setattr('acondbs.DEFAULT_CONFIG_DICT', ret)
    return ret


@pytest.fixture()
def config_path(tmp_path_factory: pytest.TempPathFactory) -> Path:
    tmpdir = tmp_path_factory.mktemp('instance')
    ret = tmpdir / 'config.py'
    ret.write_text(TEST_CONFIG_FILE_CONTENT)
    return ret


def test_create_app_default() -> None:
    app = create_app()
    assert not app.testing
    expected = dict(
        TEST_CONFIG_A='abc',
        TEST_CONFIG_B=123,
    )
    assert expected.items() <= app.config.items()


def test_create_app_config_file(config_path: Path) -> None:
    app = create_app(config_path)
    assert not app.testing
    expected = dict(
        TEST_CONFIG_A='abc',
        TEST_CONFIG_B=456,
        TEST_CONFIG_C=False,
    )
    assert expected.items() <= app.config.items()


def test_create_app_config_file_and_dict(config_path: Path) -> None:
    app = create_app(config_path, TEST_CONFIG_B=789)
    assert not app.testing
    expected = dict(
        TEST_CONFIG_A='abc',
        TEST_CONFIG_B=789,
        TEST_CONFIG_C=False,
    )
    assert expected.items() <= app.config.items()


def test_create_app_dict() -> None:
    app = create_app(TEST_CONFIG_B=789)
    assert not app.testing
    expected = dict(
        TEST_CONFIG_A='abc',
        TEST_CONFIG_B=789,
    )
    assert expected.items() <= app.config.items()
