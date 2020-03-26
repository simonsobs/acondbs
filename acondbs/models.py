from .db.sa import sa

##__________________________________________________________________||
class Simulation(sa.Model):
    __tablename__ = 'simulations'
    simulation_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    date_posted = sa.Column(sa.Date())
    mapper = sa.Column(sa.Text())
    note = sa.Column(sa.Text())

class Map(sa.Model):
    __tablename__ = 'maps'
    map_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    date_posted = sa.Column(sa.Date())
    mapper = sa.Column(sa.Text())
    note = sa.Column(sa.Text())

class Beam(sa.Model):
    __tablename__ = 'beams'
    beam_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    path = sa.Column(sa.Text())
    input_map_id = sa.Column(sa.ForeignKey('maps.map_id'))
    input_beam_id = sa.Column(sa.ForeignKey('beams.beam_id'))
    map = sa.relationship("Map", backref=sa.backref("beams"))
    parent_beam = sa.relationship(lambda: Beam, remote_side=beam_id, backref=sa.backref("child_beams"))

class MapFilePath(sa.Model):
    __tablename__ = 'map_path'
    map_file_path_id = sa.Column(sa.Integer(), primary_key=True)
    map_id = sa.Column(sa.ForeignKey('maps.map_id'))
    path = sa.Column(sa.Text())
    note = sa.Column(sa.Text())
    map = sa.relationship("Map", backref=sa.backref("map_file_paths"))

##__________________________________________________________________||
