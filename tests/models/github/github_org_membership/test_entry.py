from flask import Flask

from acondbs.db.sa import sa
from acondbs.models import GitHubOrg, GitHubOrgMembership, GitHubUser


def test_relation(app: Flask) -> None:
    with app.app_context():
        membership = GitHubOrgMembership.query.one()
        org1 = GitHubOrg.query.one()
        user1 = GitHubUser.query.one()
        assert org1 == membership.org
        assert user1 == membership.member
        assert [membership] == org1.memberships
        assert [membership] == user1.memberships


def test_cascade_delete_org(app: Flask) -> None:
    with app.app_context():
        org1 = GitHubOrg.query.filter_by(login="org1").one()
        sa.session.delete(org1)
        sa.session.commit()

    with app.app_context():
        memberships = GitHubOrgMembership.query.all()
        orgs = GitHubOrg.query.all()
        users = GitHubUser.query.all()
        assert len(memberships) == 0
        assert len(orgs) == 0
        assert len(users) == 1


def test_cascade_delete_user(app: Flask) -> None:
    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="user1").one()
        sa.session.delete(user1)
        sa.session.commit()

    with app.app_context():
        memberships = GitHubOrgMembership.query.all()
        orgs = GitHubOrg.query.all()
        users = GitHubUser.query.all()
        assert len(memberships) == 0
        assert len(orgs) == 1
        assert len(users) == 0


def test_cascade_delete_membership(app: Flask) -> None:
    with app.app_context():
        membership = GitHubOrgMembership.query.one()
        sa.session.delete(membership)
        sa.session.commit()

    with app.app_context():
        memberships = GitHubOrgMembership.query.all()
        orgs = GitHubOrg.query.all()
        users = GitHubUser.query.all()
        assert len(memberships) == 0
        assert len(orgs) == 1
        assert len(users) == 1
