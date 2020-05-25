from acondbs.db.sa import sa
from acondbs.models import Product

# These tests are written primarily for the developer to understand
# how models in flask_sqlalchemy work.

# __________________________________________________________________||
def test_simple(app):
    '''A simple test of deleting an object
    '''

    with app.app_context():

        # save the initial number of the products to compare later
        nproducts = len(Product.query.all())

    with app.app_context():
        product1 = Product.query.filter_by(product_id=1012).first()
        sa.session.delete(product1)
        sa.session.commit()

    with app.app_context():

        # test the number of the products is decreased by one
        assert (nproducts - 1) == len(Product.query.all())

        # the product is no longer found
        product1 = Product.query.filter_by(product_id=1012).first()
        assert product1 is None

# __________________________________________________________________||
