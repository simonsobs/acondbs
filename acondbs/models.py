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

##__________________________________________________________________||
class ProductType(sa.Model):
    __tablename__ = 'product_types'
    type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
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
    product = sa.relationship("Product", backref=sa.backref("paths"))

class ProductRelationType(sa.Model):
    __tablename__ = 'product_relation_types'
    type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)

class ProductRelation(sa.Model):
    __tablename__ = 'product_relations'
    relation_id = sa.Column(sa.Integer(), primary_key=True)
    type_id = sa.Column(sa.ForeignKey('product_relation_types.type_id'))
    type_ = sa.relationship("ProductRelationType")
    self_product_id = sa.Column(sa.ForeignKey('products.product_id'))
    self_ = sa.relationship("Product", foreign_keys=[self_product_id], backref=sa.backref("relations"))
    other_product_id = sa.Column(sa.ForeignKey('products.product_id'))
    other = sa.relationship("Product", foreign_keys=[other_product_id])
    reverse_relation_id = sa.Column(sa.ForeignKey('product_relations.relation_id'))
    reverse = sa.relationship(
        lambda: ProductRelation,
        uselist=False,
        foreign_keys=[reverse_relation_id],
        remote_side="ProductRelation.relation_id",
        post_update=True)

##__________________________________________________________________||
