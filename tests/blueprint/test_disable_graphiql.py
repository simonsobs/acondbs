import pytest

from acondbs import create_app
from pathlib import Path
from acondbs.db.ops import define_tables

from ..constants import SAMPLE_DIR

##__________________________________________________________________||
params = [
    [{"ACONDBS_GRAPHIQL": True}, 200, "<!DOCTYPE html>"],
    [{"ACONDBS_GRAPHIQL": False}, 400, "errors"],
]


@pytest.mark.parametrize("kwargs, code, data", params)
def test_disable_graphiql(kwargs, code, data, snapshot):
    config_path = Path(SAMPLE_DIR, "config.py")
    kwargs.update(dict(SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"))
    app = create_app(config_path, **kwargs)
    with app.app_context():
        define_tables()
    client = app.test_client()

    response = client.get("/graphql", headers={"Accept": "text/html"})
    assert code == response.status_code
    assert data in response.data.decode("utf-8")


##__________________________________________________________________||
