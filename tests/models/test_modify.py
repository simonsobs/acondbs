from acondbs.db import db
from acondbs.models import Map, Beam

# __________________________________________________________________||
def test_map_add(app):

    with app.app_context():
        map1 = Map(name="map1")
        beam1 = Beam(name="beam1", map=map1)
        db.session.add(map1)
        db.session.commit()

    with app.app_context():
        results = Map.query.all()
        assert 4 == len(results)

        map1 = Map.query.filter_by(name='map1').first()
        beam1 = Beam.query.filter_by(name='beam1').first()
        assert isinstance(map1, Map)
        assert isinstance(beam1, Beam)
        assert beam1 is map1.beams[0]

# __________________________________________________________________||
def test_map_update(app):
    with app.app_context():
        map1 = Map.query.filter_by(map_id=1012).first()
        assert 'lat20200120' == map1.name
        map1.name = 'new-map-name'
        db.session.commit()
    with app.app_context():
        map1 = Map.query.filter_by(map_id=1012).first()
        assert 'new-map-name' == map1.name

# __________________________________________________________________||
