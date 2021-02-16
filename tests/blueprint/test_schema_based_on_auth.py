from flask import json
from pathlib import Path

import pytest
import unittest.mock as mock

from acondbs import create_app
from acondbs.db.ops import define_tables

from ..constants import SAMPLE_DIR

##__________________________________________________________________||
QUERY = '''
{
  __schema {
    queryType {
      fields {
        name
      }
    }
    mutationType {
      fields {
        name
      }
    }
    subscriptionType {
      fields {
        name
      }
    }
  }
}
'''

##__________________________________________________________________||
@pytest.fixture()
def mock_auth(monkeypatch):
    y = mock.Mock()
    monkeypatch.setattr("acondbs.blueprint.auth", y)
    yield y

##__________________________________________________________________||
@pytest.mark.parametrize('is_signed_in', [True, False])
@pytest.mark.parametrize('is_admin', [True, False])
def test_schema_selection(is_signed_in, is_admin, mock_auth, snapshot):

    mock_auth.is_signed_in.return_value = is_signed_in
    mock_auth.is_admin.return_value = is_admin

    config_path = Path(SAMPLE_DIR, 'config.py')
    kwargs = {"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    app = create_app(config_path, **kwargs)
    with app.app_context():
        define_tables()
    client = app.test_client()

    response = client.get(
        '/graphql',
        query_string=dict(query=QUERY))

    assert 200 == response.status_code

    result = json.loads(response.data)['data']

    un_jsonified = json.loads(response.data)
    snapshot.assert_match(un_jsonified)
    # print(json.dumps(un_jsonified, indent=2))

##__________________________________________________________________||
