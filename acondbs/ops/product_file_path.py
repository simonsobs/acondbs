from acondbs.db.sa import sa
from acondbs.models import ProductFilePath


def create_product_file_path(**kwargs) -> ProductFilePath:
    model = ProductFilePath(**kwargs)
    sa.session.add(model)
    return model


def update_product_file_path(path_id, **kwargs) -> ProductFilePath:
    model = ProductFilePath.query.filter_by(path_id=path_id).one()
    for k, v in kwargs.items():
        setattr(model, k, v)
    return model


def delete_product_file_path(path_id) -> None:
    model = ProductFilePath.query.filter_by(path_id=path_id).one()
    sa.session.delete(model)
