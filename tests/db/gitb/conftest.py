from pathlib import Path

import pytest


##__________________________________________________________________||
@pytest.fixture()
def empty_folder(tmpdir_factory):
    """path to an empty folder
    """
    folder = Path(tmpdir_factory.mktemp('git'))
    yield folder


@pytest.fixture()
def folder(empty_folder):
    """path to an folder (not a git repo) with two text files

    f.txt
       abc

    g.txt
       123

    """
    folder = empty_folder
    file1 = folder.joinpath('f.txt')
    file2 = folder.joinpath('g.txt')
    file1.write_text('abc\n')
    file2.write_text('123\n')
    yield folder

##__________________________________________________________________||
