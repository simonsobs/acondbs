import pytest

from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import GitHubAdminAppToken

# __________________________________________________________________||
def test_token(app_empty):
    app = app_empty

    row = GitHubAdminAppToken(token="token123")

    with app.app_context():
        sa.session.add(row)
        sa.session.commit()

    with app.app_context():
        row = GitHubAdminAppToken.query.one()
        assert row.token == "token123"

# __________________________________________________________________||