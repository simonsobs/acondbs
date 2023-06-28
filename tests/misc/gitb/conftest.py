from pathlib import Path
from typing import Callable

import git
import pytest


@pytest.fixture()
def folder(tmp_path_factory: pytest.TempPathFactory) -> Path:
    '''path to an folder (not a git repo) with two text files

    f.txt
       abc

    g.txt
       123

    '''
    folder = tmp_path_factory.mktemp('git')
    file1 = folder.joinpath('f.txt')
    file2 = folder.joinpath('g.txt')
    file1.write_text('abc\n')
    file2.write_text('123\n')
    return folder


@pytest.fixture()
def repo(folder: Path) -> git.Repo:
    '''a git repo

    The folder is initialized as a git repo.
    The two files in the folder are committed.


    '''
    repo = git.Repo.init(folder)
    repo.git.add(A=True)
    repo.index.commit('initial commit')
    return repo


@pytest.fixture()
def bare_repo(repo: git.Repo, tmp_path_factory: pytest.TempPathFactory) -> git.Repo:
    '''a bare repo, a clone of the repo'''
    folder = tmp_path_factory.mktemp('git')
    assert repo.working_tree_dir
    y = git.Repo.clone_from(repo.working_tree_dir, folder, bare=True)
    return y


@pytest.fixture()
def github_repo_url(
    bare_repo: git.Repo, tmp_path_factory: pytest.TempPathFactory
) -> Callable[[], str]:
    '''a factory fixture'''
    url = 'git@github.com:TaiSakuma/fuzzy-garbanzo.git'

    def _f() -> str:
        '''create a clone of the bare repo and push force
        the content to the github repo

        '''
        folder = tmp_path_factory.mktemp('git')
        clone = git.Repo.clone_from(bare_repo.git_dir, folder)
        branch_name = clone.active_branch.name
        remote = clone.create_remote('github', url=url)
        remote.push(refspec=f'{branch_name}:{branch_name}', force=True)
        return url

    return _f


@pytest.fixture(
    params=[
        'local_folder',
        # 'github_repo'
    ]
)
def remote_url(
    request: pytest.FixtureRequest,
    bare_repo: git.Repo,
    github_repo_url: Callable[[], str],
) -> str:
    p = request.param
    if p == 'local_folder':
        y = str(bare_repo.git_dir)
    elif p == 'github_repo':
        y = github_repo_url()
    else:
        raise ValueError(f'unknown param: {p}')
    return y
