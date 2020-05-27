import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
def test_types(app, snapshot):

    query = '''
      {
        __schema {
          types {
            name
            description
            fields {
              name
              description
              type {
                name
              }
            }
            inputFields {
              name
              description
              defaultValue
            }
          }
        }
      }
    '''

    client = Client(schema)

    with app.app_context():
        result = client.execute(query, context_value={})

    assert 'errors' not in result

    snapshot.assert_match(result)

##__________________________________________________________________||
