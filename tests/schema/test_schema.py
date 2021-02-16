from .funcs import assert_query

##__________________________________________________________________||
def test_types(app, snapshot):

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

    assert_query(app, snapshot, [[query], {}])

##__________________________________________________________________||
