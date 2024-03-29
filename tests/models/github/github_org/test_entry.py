from flask import Flask

from acondbs.db.sa import sa
from acondbs.models import GitHubOrg


def test_entry(app_empty: Flask) -> None:
    app = app_empty

    row = GitHubOrg(login="urban-octo-disco", git_hub_id="012:Organization75631844")

    with app.app_context():
        sa.session.add(row)
        sa.session.commit()

    with app.app_context():
        row = GitHubOrg.query.filter_by(login="urban-octo-disco").one()
        assert "urban-octo-disco" == row.login
