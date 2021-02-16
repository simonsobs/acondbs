import pytest

from acondbs.schema import (
    schema,
    schema_public,
    schema_private,
    schema_admin
)

from .funcs import assert_query

##__________________________________________________________________||
params = [
    pytest.param(schema, id='all'),
    pytest.param(schema_public, id='public'),
    pytest.param(schema_private, id='private'),
    pytest.param(schema_admin, id='admin'),
]

@pytest.mark.parametrize('schema', params)
def test_types(schema, app, snapshot):

    query = '''
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

    assert_query(app, snapshot, [[query], {}], schema=schema)

##__________________________________________________________________||
