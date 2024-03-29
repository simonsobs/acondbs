import pytest
from flask import Flask

from acondbs.db.sa import sa
from acondbs.models import GitHubOrg, GitHubOrgMembership, GitHubUser


@pytest.fixture
def app(app_empty: Flask) -> Flask:
    y = app_empty

    org1 = GitHubOrg(login="org1", git_hub_id="012:Organization1")
    user1 = GitHubUser(login="user1", git_hub_id="04:User1")
    membership = GitHubOrgMembership(org=org1, member=user1)

    with y.app_context():
        sa.session.add(membership)
        sa.session.commit()

    return y
