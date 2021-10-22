from acondbs.db.sa import sa
from acondbs.models import Logging


##__________________________________________________________________||
def test_column(app_empty):
    app = app_empty

    with app.app_context():
        model = Logging(level="ERROR", message="an exception occured")
        sa.session.add(model)
        sa.session.commit()
        id_ = model.id_
        assert id_

    with app.app_context():
        model = Logging.query.filter_by(id_=id_).one()
        assert model.level == "ERROR"


def test_repr(app_empty):
    app = app_empty

    model = Logging(level="ERROR", message="an exception occured")
    repr(model)

    with app.app_context():
        sa.session.add(model)
        sa.session.commit()
        id_ = model.id_

    with app.app_context():
        model = Logging.query.filter_by(id_=id_).one()
        repr(model)


##__________________________________________________________________||
