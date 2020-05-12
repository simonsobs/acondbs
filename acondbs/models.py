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
class CommonFields:
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    contact = sa.Column(sa.Text())
    date_produced = sa.Column(sa.Date())
    produced_by = sa.Column(sa.Text())
    date_posted = sa.Column(sa.Date())
    posted_by = sa.Column(sa.Text())
    date_updated = sa.Column(sa.Date())
    updated_by = sa.Column(sa.Text())

##__________________________________________________________________||
class Simulation(sa.Model):
    __tablename__ = 'simulations'
    product_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    date_posted = sa.Column(sa.Date())
    mapper = sa.Column(sa.Text())
    note = sa.Column(sa.Text())

class SimulationFilePath(sa.Model):
    __tablename__ = 'simulation_file_paths'
    path_id = sa.Column(sa.Integer(), primary_key=True)
    product_id = sa.Column(sa.ForeignKey('simulations.product_id'))
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product = sa.relationship("Simulation", backref=sa.backref("simulation_file_paths"))

class Map(sa.Model, CommonFields):
    __tablename__ = 'maps'
    product_id = sa.Column(sa.Integer(), primary_key=True)
    note = sa.Column(sa.Text())

class MapFilePath(sa.Model):
    __tablename__ = 'map_file_paths'
    path_id = sa.Column(sa.Integer(), primary_key=True)
    product_id = sa.Column(sa.ForeignKey('maps.product_id'))
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product = sa.relationship("Map", backref=sa.backref("paths"))

class Beam(sa.Model):
    __tablename__ = 'beams'
    product_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    input_map_product_id = sa.Column(sa.ForeignKey('maps.product_id'))
    input_beam_product_id = sa.Column(sa.ForeignKey('beams.product_id'))
    map = sa.relationship("Map", backref=sa.backref("beams"))
    parent_beam = sa.relationship(lambda: Beam, remote_side=product_id, backref=sa.backref("child_beams"))

class BeamFilePath(sa.Model):
    __tablename__ = 'beam_file_paths'
    path_id = sa.Column(sa.Integer(), primary_key=True)
    product_id = sa.Column(sa.ForeignKey('beams.product_id'))
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    product = sa.relationship("Beam", backref=sa.backref("beam_file_paths"))

##__________________________________________________________________||
