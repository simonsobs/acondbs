import pytest

from flask_sqlalchemy import BaseQuery

from acondbs.models import Product

# These tests are written primarily for the developer to understand
# how models in flask_sqlalchemy work.

# __________________________________________________________________||
def test_context(app):

    # query cannot be accessed outside of the app context
    with pytest.raises(RuntimeError):
        Product.query

    with app.app_context():
        Product.query

def test_query_all(app):

    with app.app_context():

        # query is an instance of BaseQuery
        query = Product.query
        assert isinstance(query, BaseQuery)

        # query.all() returns a list of products
        results = query.all()
        # e.g., [<Product 1001>, <Product 1012>, <Product 1013>]

        assert isinstance(results[0], Product)

def test_query_filter(app):

    with app.app_context():

        # filter_by() returns an instance of BaseQuery
        query = Product.query.filter_by(name='lat20200120')
        assert isinstance(query, BaseQuery)

        # the results are a list with one element
        results = query.all()
        assert 1 == len(results)
        assert ['lat20200120'] == [e.name for e in results]

        # first() returns a product
        product = query.first()
        assert isinstance(product, Product)
        assert 'lat20200120' == product.name

def test_query_filter_nonexistent(app):

    with app.app_context():

        query = Product.query.filter_by(name='no-such-product')
        assert isinstance(query, BaseQuery)

        # the results are an empty list
        results = query.all()
        assert [] == results

        # first() returns None
        product = query.first()
        assert product is None

# __________________________________________________________________||
