from flask import json
import pytest

##__________________________________________________________________||
def test_graphql(client):
    response = client.get(
        '/graphql',
        query_string=dict(query='{ allProducts { edges { node { id name } } }}'))
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    # print(json.dumps(un_jsonified, indent=2))

##__________________________________________________________________||
from acondbs import create_app
from .constants import SAMPLE_DIR
from pathlib import Path
from acondbs.db.ops import define_tables

params = [
    {},
    {'ACONDBS_SCHEME_MUTATION_DISABLE': True},
    {'ACONDBS_SCHEME_MUTATION_DISABLE': False},
]

@pytest.mark.parametrize('kwargs', params)
def test_disable_mutation(kwargs, snapshot):
    config_path = Path(SAMPLE_DIR, 'config.py')
    kwargs.update(dict(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
    ))
    app = create_app(config_path, **kwargs)
    with app.app_context():
        define_tables()
    client = app.test_client()

    query = '''
        {
          Query: __type(name: "Query") {
            name
            description
            fields {
              name
            }
          }
          Mutation: __type(name: "Mutation") {
            name
            description
            fields {
              name
            }
          }
        }
    '''

    response = client.get(
        '/graphql',
        query_string=dict(query=query))
    assert 200 == response.status_code
    snapshot.assert_match(json.loads(response.data))

##__________________________________________________________________||
params = [
    [{'ACONDBS_GRAPHIQL': True}, 200, '<!DOCTYPE html>'],
    [{'ACONDBS_GRAPHIQL': False}, 400, 'errors'],
]

@pytest.mark.parametrize('kwargs, code, data', params)
def test_disable_graphiql(kwargs, code, data, snapshot):
    config_path = Path(SAMPLE_DIR, 'config.py')
    kwargs.update(dict(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
    ))
    app = create_app(config_path, **kwargs)
    with app.app_context():
        define_tables()
    client = app.test_client()

    response = client.get('/graphql', headers={"Accept": "text/html"})
    assert code == response.status_code
    assert data in response.data.decode("utf-8")

##__________________________________________________________________||
