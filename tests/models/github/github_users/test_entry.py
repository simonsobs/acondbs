import pytest

from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import GitHubUser

# __________________________________________________________________||
def test_entry(app_empty):
    app = app_empty

    row = GitHubUser(login="octocat")

    with app.app_context():
        sa.session.add(row)
        sa.session.commit()

    with app.app_context():
        row = GitHubUser.query.filter_by(login='octocat').one()
        assert 'octocat' == row.login

# __________________________________________________________________||
