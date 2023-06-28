from acondbs.db.sa import sa
from acondbs.models import Log


def create_log(**kwargs) -> Log:
    model = Log(**kwargs)
    sa.session.add(model)
    return model


def delete_log(id_) -> None:
    model = Log.query.filter_by(id_=id_).one()
    sa.session.delete(model)
