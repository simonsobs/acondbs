import pytest

from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import (
    GitHubAdminAppToken,
    GitHubUser
)

##__________________________________________________________________||
def test_query(app):

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        token1, token2 = user1.tokens

        assert token1.token == "token_001"
        assert token1.scope == "read:org"
        assert token1.user == user1

        assert token2.token == "token_002"
        assert token2.scope == "read:org"
        assert token2.user == user1

##__________________________________________________________________||
def test_add(app):

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        ntokens = len(user1.tokens) # = 2
        token3 = GitHubAdminAppToken(token="token_003", scope="read:org", user=user1)
        sa.session.commit()

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        assert ntokens + 1 == len(user1.tokens)
        assert 'token_003' in [t.token for t in user1.tokens]

##__________________________________________________________________||
def test_delete(app):

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        ntokens = len(user1.tokens) # = 2
        token1 = user1.tokens[0]
        sa.session.delete(token1)
        sa.session.commit()

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        assert ntokens - 1 == len(user1.tokens) # 1

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        token2 = user1.tokens[0]
        sa.session.delete(token2)
        sa.session.commit()

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        assert ntokens - 2 == len(user1.tokens) # 0

##__________________________________________________________________||
def test_delete_cascade(app):

    with app.app_context():
        user1 = GitHubUser.query.filter_by(login="octocat").one()
        sa.session.delete(user1)
        sa.session.commit()

    with app.app_context():
        tokens = GitHubAdminAppToken.query.all()
        assert 0 == len(tokens)

##__________________________________________________________________||
