from acondbs.db.sa import sa
from acondbs.models import Product, ProductFilePath

# These tests are written primarily for the developer to understand
# how models in flask_sqlalchemy work.

# __________________________________________________________________||
def test_simple(app):
    '''A simple test of adding an object
    '''

    with app.app_context():

        # save the initial number of the products to compare later
        nproducts = len(Product.query.all())

    # this instantiation doesn't need be within a app context
    product1 = Product(name="product1")

    with app.app_context():
        sa.session.add(product1)
        sa.session.commit()

    with app.app_context():

        # test the number of the products is increased by one
        assert (nproducts + 1) == len(Product.query.all())

        # the new product can be retrieved in a different app context
        product1_ = Product.query.filter_by(name='product1').first()
        assert isinstance(product1_, Product)

# __________________________________________________________________||
def test_python_object(app):
    '''A simple test about Python object
    '''

    product1 = Product(name="product1")

    with app.app_context():
        sa.session.add(product1)
        sa.session.commit()

        product1_ = Product.query.filter_by(name='product1').first()

        # the query returns the same Python object
        assert product1 is product1_

    with app.app_context():
        product1_ = Product.query.filter_by(name='product1').first()

        # In a different app context, no longer the same Python object
        assert product1 is not product1_

# __________________________________________________________________||
def test_primary_key(app):
    '''A simple test about the primary key
    '''

    product1 = Product(name="product1")

    # The primary key (product_id) is None at this point
    assert product1.product_id is None

    with app.app_context():
        sa.session.add(product1)
        sa.session.commit()

        # After the commit, product_id is automatically assigned
        product_id = product1.product_id
        assert product_id is not None

    with app.app_context():

        # The object can be retrived by the product_id in another context
        product1 = Product.query.filter_by(product_id=product_id).first()
        assert 'product1' == product1.name

# __________________________________________________________________||
def test_relation(app):
    '''A simple test of adding an object with relation
    '''

    product1 = Product(name="product1")
    path1 = ProductFilePath(path="/a/b/c", product=product1)

    # The relation has been already established
    assert product1 is path1.product
    assert [path1] == product1.paths

    # The primary and foreign keys are still None
    assert product1.product_id is None
    assert path1.path_id is None
    assert path1.product_id is None

    with app.app_context():
        sa.session.add(product1)
        sa.session.commit()

        # The primary keys are assigned
        assert product1.product_id is not None
        assert path1.path_id is not None

        # The foreign key is correctly set
        assert product1.product_id == path1.product_id

    with app.app_context():
        product1 = Product.query.filter_by(name='product1').first()

        # The relation is preserved in a different app context
        path1 = product1.paths[0]
        assert "/a/b/c" == path1.path
        assert product1 is path1.product
        assert product1.product_id == path1.product_id

# __________________________________________________________________||
