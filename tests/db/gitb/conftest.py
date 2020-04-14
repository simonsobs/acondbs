from pathlib import Path
import git

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
@pytest.fixture()
def repo(folder):
    """a git repo

    The folder is initialized as a git repo.
    The two files in the folder are committed.


    """
    repo = git.Repo.init(folder)
    repo.git.add(A=True)
    repo.index.commit('initial commit')
    yield repo

##__________________________________________________________________||
