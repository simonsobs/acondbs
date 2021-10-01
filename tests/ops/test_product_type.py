import pytest

from sqlalchemy import exc

from acondbs import ops
from acondbs.models import ProductType


##__________________________________________________________________||
params = [
    pytest.param(None, [], id="none"),
    pytest.param([], [], id="empty"),
    pytest.param([2], ["produced_by"], id="one"),
    pytest.param(
        [1, 2, 3], ["contact", "produced_by", "date_produced"], id="three"
    ),
    pytest.param(
        [2, 3, 3, 1, 2, 3, 1, 1],
        ["contact", "produced_by", "date_produced"],
        id="unsorted-duplicate",
    ),
]


@pytest.mark.parametrize("field_ids, expected_field_names", params)
def test_create_product_type(app, field_ids, expected_field_names):

    with app.app_context():
        model = ops.create_product_type(
            name="derived_map",
            order=3,
            indef_article="a",
            singular="derived map",
            plural="derived maps",
            icon="mdi-map-clock",
            field_ids=field_ids,
        )
        ops.commit()

    with app.app_context():
        model = ProductType.query.filter_by(name="derived_map").one()
        actual_field_names = [f.field.name for f in model.fields]
        assert actual_field_names == expected_field_names


params = [
    pytest.param([1, 2, 3, 88], id="non-existent"),
]


@pytest.mark.parametrize("field_ids", params)
def test_create_product_type_error(app, field_ids):

    with app.app_context():
        with pytest.raises(exc.NoResultFound):
            model = ops.create_product_type(
                name="derived_map",
                order=3,
                indef_article="a",
                singular="derived map",
                plural="derived maps",
                icon="mdi-map-clock",
                field_ids=field_ids,
            )
        ops.commit()

    with app.app_context():
        model = ProductType.query.filter_by(name="derived_map").one_or_none()
        assert model is None


##__________________________________________________________________||
