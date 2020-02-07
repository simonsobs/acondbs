from acondbs.schema import schema

##__________________________________________________________________||
def test_schema(app):
    with app.app_context():
        query = '{ allMaps { edges { node {name} } }}'
        result = schema.execute(query)
        assert result.errors is None
        assert 15 == len(result.data['allMaps']['edges'])

##__________________________________________________________________||
def test_sort(app):
    with app.app_context():
        query = '{ allMaps(sort: DATE_POSTED_DESC) { edges { node {name} } }}'
        result = schema.execute(query)
        assert result.errors is None
        assert 15 == len(result.data['allMaps']['edges'])
        print(result.data)

##__________________________________________________________________||
