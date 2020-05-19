import pytest
from graphene.test import Client

from acondbs.schema.schema import schema

##__________________________________________________________________||
params = [
    pytest.param(
        '''
          {
            allProductRelationTypes {
              edges {
                node {
                  typeId
                  name
                }
              }
            }
          }
         ''',
        id='allProductRelationTypes'
    ),
    pytest.param(
        '''
          {
            productRelationType(typeId: 1) {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-TypeId-one)'
    ),
    pytest.param(
        '''
          {
            productRelationType(name: "parent") {
              typeId
              name
            }
          }
         ''',
        id='productRelationType-by-name-parent)'
    ),
]

@pytest.mark.parametrize('query', params)
def test_schema(app, snapshot, query):
    client = Client(schema)
    with app.app_context():
        result = client.execute(query)
        assert 'errors' not in result
        snapshot.assert_match(result)

##__________________________________________________________________||
