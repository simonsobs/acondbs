from flask import Flask

from acondbs.models import ProductRelation


def test_repr(app: Flask) -> None:
    with app.app_context():
        model = ProductRelation.query.filter_by(relation_id=1).one()
        repr(model)


def test_transient(app: Flask) -> None:
    model = ProductRelation()
    repr(model)
