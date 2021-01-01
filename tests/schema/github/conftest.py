from pathlib import Path
import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import (
    GitHubToken,
    GitHubUser,
    GitHubOrg
)

from ...constants import SAMPLE_DIR

##__________________________________________________________________||
@pytest.fixture
def app_empty():
    config_path = Path(SAMPLE_DIR, 'config.py')
    database_uri ="sqlite:///:memory:"
    y = create_app(config_path=config_path, SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y

@pytest.fixture
def app(app_empty):

    y = app_empty

    #
    #  +-------+        +--------+
    #  | user1 | --+--> | token1 |
    #  +-------+   |    +--------+
    #              |
    #              |    +--------+
    #              +--> | token2 |
    #                   +--------+
    #
    #
    #  +------+
    #  | org1 |
    #  +------+
    #

    user1 = GitHubUser(login="octocat")
    token1 = GitHubToken(token="token_001", scope="read:org", user=user1)
    token2 = GitHubToken(token="token_002", scope="read:org", user=user1)

    org1 = GitHubOrg(login="org1")

    with y.app_context():
        sa.session.add(user1)
        sa.session.add(org1)
        sa.session.commit()
    yield y

# __________________________________________________________________||
