import pytest

from acondbs import create_app
from acondbs.db.ops import define_tables

##__________________________________________________________________||
params = [
    [None, "//cdn.jsdelivr.net/npm/graphiql@0.11.11/graphiql.min.js"],
    [1, "https://unpkg.com/graphiql/graphiql.min.js"],
    [2, "graphql-playground"],
]


@pytest.mark.parametrize("number, data", params)
def test_disable_graphiql(number, data):
    app = create_app(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        ACONDBS_GRAPHIQL=True,
        ACONDBS_GRAPHIQL_TEMPLATE_NO=number,
    )
    with app.app_context():
        define_tables()

    client = app.test_client()

    response = client.get("/graphql", headers={"Accept": "text/html"})
    assert 200 == response.status_code
    assert data in response.data.decode("utf-8")


##__________________________________________________________________||
