import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import GitHubAcceptedOrg, GitHubUser, GitHubOrgMembership

##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri ="sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y

# __________________________________________________________________||
@pytest.fixture
def app(app_empty):
    y = app_empty

    org1 = GitHubAcceptedOrg(login="org1")
    user1 = GitHubUser(login="user1")
    membership = GitHubOrgMembership(org=org1, member=user1)

    with y.app_context():
        sa.session.add(membership)
        sa.session.commit()
    yield y

# __________________________________________________________________||
