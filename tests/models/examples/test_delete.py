import pytest
from flask import Flask

from acondbs.db.sa import sa
from acondbs.models import Product, ProductType

# These tests are written primarily for the developer to understand
# how models in flask_sqlalchemy work.


@pytest.fixture
def app(app: Flask) -> Flask:
    y = app

    type_map = ProductType(name='map')
    map1 = Product(name='map1', type_=type_map)  # noqa: F841
    map2 = Product(name='map2', type_=type_map)  # noqa: F841
    map3 = Product(name='map3', type_=type_map)  # noqa: F841

    with y.app_context():
        sa.session.add(type_map)
        sa.session.commit()

    return y


def test_simple(app: Flask) -> None:
    '''A simple test of deleting an object'''

    with app.app_context():
        assert 3 == len(Product.query.all())

    with app.app_context():
        product1 = Product.query.filter_by(name='map1').first()
        sa.session.delete(product1)
        sa.session.commit()

    with app.app_context():
        assert 2 == len(Product.query.all())

        # the product is no longer found
        product1 = Product.query.filter_by(name='map1').first()
        assert product1 is None
