from pathlib import Path

import pytest


##__________________________________________________________________||
@pytest.fixture()
def folder(tmpdir_factory):
    """path to an folder (not a git repo) with two text files

    f.txt
       abc

    g.txt
       123

    """
    folder = Path(tmpdir_factory.mktemp('git'))
    file1 = folder.joinpath('f.txt')
    file2 = folder.joinpath('g.txt')
    file1.write_text('abc\n')
    file2.write_text('123\n')
    yield folder

##__________________________________________________________________||
