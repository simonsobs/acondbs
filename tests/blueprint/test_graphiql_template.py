from flask import json
import pytest

from acondbs import create_app
from pathlib import Path
from acondbs.db.ops import define_tables

from ..constants import SAMPLE_DIR

##__________________________________________________________________||
params = [
    [{'ACONDBS_GRAPHIQL_TEMPLATE_NO': None}, '//cdn.jsdelivr.net/npm/graphiql@0.11.11/graphiql.min.js'],
    [{'ACONDBS_GRAPHIQL_TEMPLATE_NO': 1}, 'https://unpkg.com/graphiql/graphiql.min.js'],
    [{'ACONDBS_GRAPHIQL_TEMPLATE_NO': 2}, 'graphql-playground'],
]

@pytest.mark.parametrize('kwargs, data', params)
def test_disable_graphiql(kwargs, data, snapshot):
    config_path = Path(SAMPLE_DIR, 'config.py')
    kwargs.update(dict(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
    ))
    app = create_app(config_path, **kwargs)
    with app.app_context():
        define_tables()
    client = app.test_client()

    response = client.get('/graphql', headers={"Accept": "text/html"})
    assert 200 == response.status_code
    assert data in response.data.decode("utf-8")

##__________________________________________________________________||
