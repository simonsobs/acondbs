import flask_sqlalchemy

from acondbs.db import db
from acondbs import models

# These tests are written primarily for the developer to understand
# how models in flask_sqlalchemy work.

# __________________________________________________________________||
def test_map_query_all(app):
    with app.app_context():
        query = models.Map.query
        assert isinstance(query, flask_sqlalchemy.BaseQuery)

        results = query.all()
        assert 3 == len(results)
        assert ['lat20190213', 'lat20200120', 'lat20200201'] == [
            e.name for e in results]


def test_map_query_filter_by_name_none(app):
    with app.app_context():
        query = models.Map.query.filter_by(name='no-such-map')
        assert isinstance(query, flask_sqlalchemy.BaseQuery)

        results = query.all()
        assert 0 == len(results)

        map = query.first()
        assert map is None


def test_map_query_filter_by_name(app):
    with app.app_context():
        query = models.Map.query.filter_by(name='lat20200120')
        assert isinstance(query, flask_sqlalchemy.BaseQuery)

        results = query.all()
        assert 1 == len(results)
        assert ['lat20200120'] == [e.name for e in results]

        map = query.first()
        assert isinstance(map, models.Map)
        assert 'lat20200120' == map.name

        assert 1 == len(map.beams)

        beam = map.beams[0]

        assert '20200123' == beam.name

        assert map is beam.map

# __________________________________________________________________||
def test_backref(app):
    with app.app_context():

        map1 = models.Map(name="map1")
        assert 0 == len(map1.beams)

        beam1 = models.Beam(name="beam1", map=map1)
        assert 1 == len(map1.beams)
        assert beam1 is map1.beams[0]
        assert map1 is beam1.map
        assert 0 == len(beam1.child_beams)

        beam2 = models.Beam(name="beam2", map=map1, parent_beam=beam1)
        assert 2 == len(map1.beams)
        assert beam2 is map1.beams[1]
        assert map1 is beam2.map
        assert beam1 is beam2.parent_beam
        assert 1 == len(beam1.child_beams)
        assert beam2 is beam1.child_beams[0]

# __________________________________________________________________||
def test_map_add(app):

    with app.app_context():
        map1 = models.Map(name="map1")
        beam1 = models.Beam(name="beam1", map=map1)
        db.session.add(map1)
        db.session.commit()

    with app.app_context():
        results = models.Map.query.all()
        assert 4 == len(results)

        map1 = models.Map.query.filter_by(name='map1').first()
        beam1 = models.Beam.query.filter_by(name='beam1').first()
        assert isinstance(map1, models.Map)
        assert isinstance(beam1, models.Beam)
        assert beam1 is map1.beams[0]

