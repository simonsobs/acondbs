import git
import pytest
from flask import Flask
from graphene.test import Client

from acondbs.db.backup import backup_db_as_csv_to_github_
from acondbs.db.ops import export_db_to_csv_files
from acondbs.schema import schema_admin


@pytest.fixture
def local_repo(app: Flask, tmp_path_factory: pytest.TempPathFactory) -> git.Repo:
    # create a local repo with CSV files
    local_folder = tmp_path_factory.mktemp('backup')
    with app.app_context():
        export_db_to_csv_files(local_folder)
    local_repo = git.Repo.init(local_folder)
    local_repo.git.add(A=True)
    local_repo.index.commit('initial commit')

    return local_repo


@pytest.fixture
def remote_repo(
    local_repo: git.Repo, tmp_path_factory: pytest.TempPathFactory
) -> git.Repo:
    '''remote repo'''

    # create a remote repo (bare repo)
    folder = tmp_path_factory.mktemp('backup')
    remote_repo = git.Repo.init(folder, bare=True)
    remote_url = remote_repo.git_dir

    # push the current branch of the local repo to the remote repo
    remote = local_repo.create_remote('origin', url=str(remote_url))
    branch_name = local_repo.active_branch.name
    remote.push(refspec='{}:{}'.format(branch_name, branch_name))
    local_repo.heads[branch_name].set_tracking_branch(remote.refs[branch_name])

    return remote_repo


def test_backup_db_as_csv_to_github_(
    app: Flask, local_repo: git.Repo, remote_repo: git.Repo
) -> None:
    repo_path = local_repo.working_tree_dir
    assert repo_path
    head_sha_old = local_repo.head.commit.hexsha
    assert head_sha_old == remote_repo.head.commit.hexsha

    # change the DB content
    mutation = '''
          mutation m {
            deleteProduct(productId: 1001) {
              ok
            }
          }
        '''
    client = Client(schema_admin)
    with app.app_context():
        result = client.execute(mutation, context_value={})
        assert 'errors' not in result

    # take backup
    with app.app_context():
        backup_db_as_csv_to_github_(repo_path)

    # assert
    assert not local_repo.is_dirty(untracked_files=True)
    head_sha_new = local_repo.head.commit.hexsha
    assert not head_sha_old == head_sha_new
    assert head_sha_new == remote_repo.head.commit.hexsha
