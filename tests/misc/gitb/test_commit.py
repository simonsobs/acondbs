import warnings
from pathlib import Path

import git
import pytest

from acondbs.misc import gitb


def test_empty_folder(tmp_path_factory: pytest.TempPathFactory) -> None:
    '''assert empty folder won't be initialized as a repo'''
    folder = tmp_path_factory.mktemp('git')
    with warnings.catch_warnings(record=True) as w:
        gitb.commit(folder)
    assert len(w) == 1
    assert not gitb.is_git_repo(folder)


@pytest.fixture()
def nonexistent_path(tmpdir_factory: pytest.TempPathFactory) -> Path:
    '''path to a nonexistent file'''
    folder = tmpdir_factory.mktemp('git')
    path = folder / 'nonexistent'
    return path


def test_nonexistent_path(nonexistent_path: Path) -> None:
    '''assert exception is raised for nonexistent path'''
    with pytest.raises(ValueError):
        gitb.commit(nonexistent_path)


def test_non_empty_folder(folder: Path) -> None:
    '''assert a repo initialized and files committed'''
    gitb.commit(folder)
    repo = git.Repo(folder)
    assert not repo.is_dirty(untracked_files=True)
    ncommits = len(list(repo.iter_commits()))
    assert 1 == ncommits


def test_clean_repo(repo: git.Repo) -> None:
    '''assert no empty commit is made'''
    folder = repo.working_tree_dir
    assert folder
    with warnings.catch_warnings(record=True) as w:
        gitb.commit(folder)
    assert len(w) == 1
    assert not repo.is_dirty(untracked_files=True)
    ncommits = len(list(repo.iter_commits()))
    assert 1 == ncommits


@pytest.fixture()
def repo_dirty(repo: git.Repo) -> git.Repo:
    '''a dirty repo

    The repo contains a staged file, a modified file, a deleted file,
    and an untracked file.

    '''
    assert repo.working_tree_dir
    folder = Path(repo.working_tree_dir)
    file1 = folder.joinpath('f.txt')
    file2 = folder.joinpath('g.txt')
    file3 = folder.joinpath('h.txt')
    file1.write_text('xyz')
    repo.git.add(file1)
    file1.write_text('zzz')
    file2.unlink()
    file3.write_text('qwe')
    return repo


def test_dirty_repo(repo_dirty: git.Repo) -> None:
    '''assert all changes commit'''
    repo = repo_dirty
    folder = repo.working_tree_dir
    assert folder
    gitb.commit(folder)
    assert not repo.is_dirty(untracked_files=True)
    ncommits = len(list(repo.iter_commits()))
    assert 2 == ncommits


def test_default_message(repo_dirty: git.Repo) -> None:
    repo = repo_dirty
    folder = repo.working_tree_dir
    assert folder
    gitb.commit(folder)
    assert 'commit all' == repo.head.commit.message


def test_custom_message(repo_dirty: git.Repo) -> None:
    repo = repo_dirty
    folder = repo.working_tree_dir
    assert folder
    gitb.commit(folder, 'custom message')
    assert 'custom message' == repo.head.commit.message
