from flask import json
import pytest

##__________________________________________________________________||
def test_graphql(client):
    response = client.get(
        '/graphql',
        query_string=dict(query='{allMaps { edges { node { id name } } }}'))
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    # print(json.dumps(un_jsonified, indent=2))

##__________________________________________________________________||
