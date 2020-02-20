from .db.db import db

##__________________________________________________________________||
class Map(db.Model):
    __tablename__ = 'maps'
    map_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False, unique=True, index=True)
    date_posted = db.Column(db.Date())
    mapper = db.Column(db.Text())
    note = db.Column(db.Text())

class Beam(db.Model):
    __tablename__ = 'beams'
    beam_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text(), nullable=False, unique=True, index=True)
    path = db.Column(db.Text())
    input_map_id = db.Column(db.ForeignKey('maps.map_id'))
    input_beam_id = db.Column(db.ForeignKey('beams.beam_id'))
    map = db.relationship("Map", backref=db.backref("beams"))
    parent_beam = db.relationship(lambda: Beam, remote_side=beam_id, backref=db.backref("child_beams"))

class MapFilePath(db.Model):
    __tablename__ = 'map_path'
    map_file_path_id = db.Column(db.Integer(), primary_key=True)
    map_id = db.Column(db.ForeignKey('maps.map_id'))
    path = db.Column(db.Text())
    note = db.Column(db.Text())
    map = db.relationship("Map", backref=db.backref("map_file_paths"))

##__________________________________________________________________||
