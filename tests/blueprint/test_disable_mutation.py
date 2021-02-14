from flask import json
import pytest

from acondbs import create_app
from pathlib import Path
from acondbs.db.ops import define_tables

from ..constants import SAMPLE_DIR

##__________________________________________________________________||
params = [
    [{'ACONDBS_SCHEME_MUTATION_DISABLE': True}, False],
    [{'ACONDBS_SCHEME_MUTATION_DISABLE': False}, True]
]

@pytest.mark.parametrize('kwargs, mutation', params)
def test_disable_mutation(kwargs, mutation):
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
            fields {
              name
            }
          }
          Mutation: __type(name: "Mutation") {
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

    result = json.loads(response.data)['data']
    assert result['Query']
    assert mutation == bool(result['Mutation'])

##__________________________________________________________________||
