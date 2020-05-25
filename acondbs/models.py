"""declare ORM models

In this module, ORM (Object-relational mapping) models are declared.
One model is mapped to one table in the DB. Models are declared as
Python classes inheriting the Model class in Flask-SQLAlchemy.

"Declaring Models" in Flask-SQLAlchemy doc:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

"Declare a Mapping" in SQLAlchemy doc:
https://docs.sqlalchhttps://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping

"""

from .db.sa import sa

from sqlalchemy.event import listens_for

##__________________________________________________________________||
class ProductType(sa.Model):
    __tablename__ = 'product_types'
    type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    order = sa.Column(sa.Integer())
    indef_article = sa.Column(sa.Text())
    singular = sa.Column(sa.Text())
    plural = sa.Column(sa.Text())
    icon = sa.Column(sa.Text())

class Product(sa.Model):
    __tablename__ = 'products'
    product_id = sa.Column(sa.Integer(), primary_key=True)
    type_id = sa.Column(sa.ForeignKey('product_types.type_id'))
    type_ = sa.relationship("ProductType", backref=sa.backref("products"))
    name = sa.Column(sa.Text(), nullable=False)
    contact = sa.Column(sa.Text())
    date_produced = sa.Column(sa.Date())
    produced_by = sa.Column(sa.Text())
    date_posted = sa.Column(sa.Date())
    posted_by = sa.Column(sa.Text())
    date_updated = sa.Column(sa.Date())
    updated_by = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    __table_args__ = (sa.UniqueConstraint('type_id', 'name', name='_type_id_name'), )

class ProductFilePath(sa.Model):
    __tablename__ = 'product_file_paths'
    path_id = sa.Column(sa.Integer(), primary_key=True)
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product_id = sa.Column(sa.ForeignKey('products.product_id'))
    product = sa.relationship(
        "Product",
        backref=sa.backref("paths", cascade="all, delete-orphan"))

class ProductRelationType(sa.Model):
    __tablename__ = 'product_relation_types'
    type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    reverse_type_id = sa.Column(sa.ForeignKey('product_relation_types.type_id'))
    reverse = sa.relationship(
        lambda: ProductRelationType,
        uselist=False,
        foreign_keys=[reverse_type_id],
        remote_side="ProductRelationType.type_id",
        cascade="all",
        post_update=True)

##__________________________________________________________________||
class ProductRelation(sa.Model):
    __tablename__ = 'product_relations'
    relation_id = sa.Column(sa.Integer(), primary_key=True)
    type_id = sa.Column(sa.ForeignKey('product_relation_types.type_id'))
    type_ = sa.relationship("ProductRelationType")
    self_product_id = sa.Column(sa.ForeignKey('products.product_id'))
    self_ = sa.relationship(
        "Product",
        foreign_keys=[self_product_id],
        backref=sa.backref("relations", cascade="all, delete-orphan"))
    other_product_id = sa.Column(sa.ForeignKey('products.product_id'))
    other = sa.relationship("Product", foreign_keys=[other_product_id])
    reverse_relation_id = sa.Column(sa.ForeignKey('product_relations.relation_id'))
    reverse = sa.relationship(
        lambda: ProductRelation,
        uselist=False,
        foreign_keys=[reverse_relation_id],
        remote_side="ProductRelation.relation_id",
        cascade="all",
        post_update=True)

@listens_for(ProductRelation.type_, 'set')
def set_reverse_type(target, value, oldvalue, initiator):
    relation = target

    try:
        if relation.reverse.__avoid_recursive:
            return
    except:
        pass

    if not value.reverse:
        return

    if not relation.reverse:
        reverse = ProductRelation()
        reverse.reverse = relation
        relation.reverse = reverse
        relation.reverse.__avoid_recursive = True
        if relation.self_:
            reverse.other = relation.self_
        if relation.other:
            reverse.self_ = relation.other
        del relation.reverse.__avoid_recursive
    if not relation.reverse.type_:
        relation.reverse.__avoid_recursive = True
        relation.reverse.type_ = value.reverse
        del relation.reverse.__avoid_recursive

@listens_for(ProductRelation.self_, 'set')
def set_reverse_other(target, value, oldvalue, initiator):
    relation = target

    if not relation.reverse:
        return

    try:
        if relation.reverse.__avoid_recursive:
            return
    except:
        pass

    if not relation.reverse.other:
        relation.reverse.__avoid_recursive = True
        relation.reverse.other = value
        del relation.reverse.__avoid_recursive

@listens_for(ProductRelation.other, 'set')
def set_reverse_self(target, value, oldvalue, initiator):
    relation = target

    if not relation.reverse:
        return

    try:
        if relation.reverse.__avoid_recursive:
            return
    except:
        pass

    if not relation.reverse.self_:
        relation.reverse.__avoid_recursive = True
        relation.reverse.self_ = value
        del relation.reverse.__avoid_recursive

##__________________________________________________________________||
