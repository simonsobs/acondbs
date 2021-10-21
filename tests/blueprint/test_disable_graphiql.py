import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables


##__________________________________________________________________||
params = [
    [True, 200, "<!DOCTYPE html>"],
    [False, 400, "errors"],
]


@pytest.mark.parametrize("graphiql, code, data", params)
def test_disable_graphiql(graphiql, code, data):
    app = create_app(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        ACONDBS_GRAPHIQL=graphiql,
        ACONDBS_GRAPHIQL_TEMPLATE_NO=2,
    )
    with app.app_context():
        define_tables()

    client = app.test_client()

    response = client.get("/graphql", headers={"Accept": "text/html"})
    assert code == response.status_code
    assert data in response.data.decode("utf-8")


##__________________________________________________________________||
