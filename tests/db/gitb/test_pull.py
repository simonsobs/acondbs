import git
from pathlib import Path

import pytest

from acondbs.db import gitb

##__________________________________________________________________||
@pytest.fixture()
def bare_repo(repo, tmpdir_factory):
    """a bare repo, a clone of the repo
    """
    folder = Path(tmpdir_factory.mktemp('git'))
    y = git.Repo.clone_from(repo.working_tree_dir, folder, bare=True)
    yield y

@pytest.fixture()
def github_repo_url(bare_repo, tmpdir_factory):
    """a factory fixture
    """
    url = 'git@github.com:TaiSakuma/fuzzy-garbanzo.git'
    def _f():
        """create a clone of the bare repo and push force
           the content to the github repo

        """
        folder = Path(tmpdir_factory.mktemp('git'))
        clone = git.Repo.clone_from(bare_repo.git_dir, folder)
        branch_name = clone.active_branch.name
        remote = clone.create_remote('github', url=url)
        remote.push(refspec='{}:{}'.format(branch_name, branch_name), force=True)
        return url
    yield _f

@pytest.fixture(params=[
    'local_folder',
    # 'github_repo'
])
def remote_url(request, bare_repo, github_repo_url):
    p = request.param
    if p == 'local_folder':
        y = bare_repo.git_dir
    elif p == 'github_repo':
        y = github_repo_url()
    else:
        raise ValueError('unknown param: {}'.format(p))
    yield y

##__________________________________________________________________||
def test_pull(remote_url, tmpdir_factory):
    """test pull()

    """

    # create two clones
    folder1 = Path(tmpdir_factory.mktemp('git'))
    repo1 = git.Repo.clone_from(remote_url, folder1)

    folder2 = Path(tmpdir_factory.mktemp('git'))
    repo2 = git.Repo.clone_from(remote_url, folder2)

    # push a commit from repo1
    file1 = folder1.joinpath('f.txt')
    with file1.open("a") as f:
        f.write('1')
    repo1.git.add(A=True)
    repo1.index.commit('update')
    remote1 = repo1.remotes[repo1.active_branch.tracking_branch().remote_name]
    remote1.push()
    head_sha_repo1 = repo1.head.commit.hexsha

    # save sha
    head_sha_old = repo2.head.commit.hexsha

    # call pull()
    gitb.pull(folder2)

    # assert
    head_sha_new = repo2.head.commit.hexsha
    assert not head_sha_old == head_sha_new
    assert head_sha_repo1 == head_sha_new

##__________________________________________________________________||
def test_nonexistent_path(tmpdir_factory):
    """assert exception is raised for nonexistent path
    """
    folder = Path(tmpdir_factory.mktemp('git'))
    path = folder.joinpath('nonexistent')

    with pytest.raises(ValueError):
        gitb.pull(path)

def test_path_not_repo(folder):
    """assert exception is raised if not a repo
    """

    with pytest.raises(ValueError):
        gitb.pull(folder)

def test_repo_no_remote(repo):
    """assert exception is raised if a repo has no tracking branch
    """

    with pytest.raises(ValueError):
        gitb.pull(repo.working_tree_dir)

##__________________________________________________________________||
