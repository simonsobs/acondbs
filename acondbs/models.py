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
    product_type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)

class Product(sa.Model):
    __tablename__ = 'products'
    product_id = sa.Column(sa.Integer(), primary_key=True)
    product_type_id = sa.Column(sa.ForeignKey('product_types.product_type_id'))
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    contact = sa.Column(sa.Text())
    date_produced = sa.Column(sa.Date())
    produced_by = sa.Column(sa.Text())
    date_posted = sa.Column(sa.Date())
    posted_by = sa.Column(sa.Text())
    date_updated = sa.Column(sa.Date())
    updated_by = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product_type = sa.relationship("ProductType", backref=sa.backref("products"))

class ProductFilePath(sa.Model):
    __tablename__ = 'product_file_paths'
    path_id = sa.Column(sa.Integer(), primary_key=True)
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product_id = sa.Column(sa.ForeignKey('products.product_id'))
    product = sa.relationship("Product", backref=sa.backref("paths"))

##__________________________________________________________________||
class CommonProductFields:
    product_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    contact = sa.Column(sa.Text())
    date_produced = sa.Column(sa.Date())
    produced_by = sa.Column(sa.Text())
    date_posted = sa.Column(sa.Date())
    posted_by = sa.Column(sa.Text())
    date_updated = sa.Column(sa.Date())
    updated_by = sa.Column(sa.Text())
    note = sa.Column(sa.Text())

class CommonFilePathFields:
    path_id = sa.Column(sa.Integer(), primary_key=True)
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())

##__________________________________________________________________||
class Simulation(sa.Model, CommonProductFields):
    __tablename__ = 'simulations'

class SimulationFilePath(sa.Model, CommonFilePathFields):
    __tablename__ = 'simulation_file_paths'
    product_id = sa.Column(sa.ForeignKey('simulations.product_id'))
    product = sa.relationship("Simulation", backref=sa.backref("paths"))

##__________________________________________________________________||
class Map(sa.Model, CommonProductFields):
    __tablename__ = 'maps'

class MapFilePath(sa.Model, CommonFilePathFields):
    __tablename__ = 'map_file_paths'
    product_id = sa.Column(sa.ForeignKey('maps.product_id'))
    product = sa.relationship("Map", backref=sa.backref("paths"))

##__________________________________________________________________||
class Beam(sa.Model, CommonProductFields):
    __tablename__ = 'beams'
    input_map_product_id = sa.Column(sa.ForeignKey('maps.product_id'))
    input_beam_product_id = sa.Column(sa.ForeignKey('beams.product_id'))
    map = sa.relationship("Map", backref=sa.backref("beams"))
    parent_beam = sa.relationship(lambda: Beam, remote_side="Beam.product_id", backref=sa.backref("child_beams"))


class BeamFilePath(sa.Model, CommonFilePathFields):
    __tablename__ = 'beam_file_paths'
    product_id = sa.Column(sa.ForeignKey('beams.product_id'))
    product = sa.relationship("Beam", backref=sa.backref("paths"))

##__________________________________________________________________||
