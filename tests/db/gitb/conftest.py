from pathlib import Path

import pytest


##__________________________________________________________________||
@pytest.fixture()
def empty_folder(tmpdir_factory):
    """path to an empty folder
    """
    folder = Path(tmpdir_factory.mktemp('git'))
    yield folder


##__________________________________________________________________||
