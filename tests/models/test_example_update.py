from acondbs.db.sa import sa
from acondbs.models import Product

# __________________________________________________________________||
def test_simple(app):
    '''A simple test of updating an object
    '''

    with app.app_context():
        product1 = Product.query.filter_by(product_id=1012).first()
        assert 'lat20200120' == product1.name
        product1.name = 'new-product-name'
        sa.session.commit()

    with app.app_context():
        product1 = Product.query.filter_by(product_id=1012).first()
        assert 'new-product-name' == product1.name

# __________________________________________________________________||
