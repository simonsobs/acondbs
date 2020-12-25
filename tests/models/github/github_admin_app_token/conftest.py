import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import (
    GitHubAdminAppToken,
    GitHubUser
)

##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri ="sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
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

    user1 = GitHubUser(login="octocat")
    token1 = GitHubAdminAppToken(token="token_001", scope="read:org", user=user1)
    token2 = GitHubAdminAppToken(token="token_002", scope="read:org", user=user1)

    with y.app_context():
        sa.session.add(user1)
        sa.session.commit()
    yield y

# __________________________________________________________________||