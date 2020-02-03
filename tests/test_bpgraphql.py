from flask import json
import pytest

##__________________________________________________________________||
def test_graphql(client):
    response = client.get('/graphql')
    assert 200 == response.status_code

##__________________________________________________________________||
