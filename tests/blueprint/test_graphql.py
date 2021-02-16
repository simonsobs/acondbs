from flask import json
import pytest


QUERY = """{
  webConfig {
    headTitle
    toolbarTitle
  }
}"""


##__________________________________________________________________||
def test_graphql(client, snapshot):
    response = client.get(
        '/graphql',
        query_string=dict(query=QUERY))
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    snapshot.assert_match(un_jsonified)
    # print(json.dumps(un_jsonified, indent=2))

##__________________________________________________________________||
