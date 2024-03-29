from flask import json
from flask.testing import FlaskClient
from snapshottest.pytest import PyTestSnapshotTest

QUERY = '''{
  webConfig {
    id_
    json
  }
}'''


def test_graphql(client: FlaskClient, snapshot: PyTestSnapshotTest) -> None:
    print(snapshot)
    print(type(snapshot))
    path = '/graphql'

    response = client.get(path, query_string=dict(query=QUERY))
    assert 200 == response.status_code

    un_jsonified = json.loads(response.data)
    snapshot.assert_match(un_jsonified)
    # print(json.dumps(un_jsonified, indent=2))
