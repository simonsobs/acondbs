import pytest

from sqlalchemy import exc

from acondbs import ops
from acondbs.models import ProductType, TypeFieldAssociation


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
        count = ProductType.query.count()

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
        assert ProductType.query.count() == (count + 1)
        model = ProductType.query.filter_by(name="derived_map").one()
        actual_field_names = [f.field.name for f in model.fields]
        assert actual_field_names == expected_field_names


params = [
    pytest.param([1, 2, 3, 88], id="non-existent"),
]


@pytest.mark.parametrize("field_ids", params)
def test_create_product_type_error(app, field_ids):

    with app.app_context():
        count = ProductType.query.count()

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
        assert ProductType.query.count() == count
        model = ProductType.query.filter_by(name="derived_map").one_or_none()
        assert model is None


##__________________________________________________________________||
# fmt: off
params = [
    pytest.param(None, ["contact", "produced_by", "date_produced"], id="none"),
    pytest.param([], [], id="empty"),
    pytest.param([2], ["produced_by"], id="removed"),
    pytest.param(
        [1, 2, 3, 4, 5],
        ["contact", "produced_by", "date_produced", "field_four", "field_five"],
        id="added",
    ),
    pytest.param(
        [1, 4, 5],
        ["contact", "field_four", "field_five"],
        id="removed-added",
    ),
    pytest.param(
        [4, 5, 5, 5, 1, 4, 5, 1, 1],
        ["contact", "field_four", "field_five"],
        id="removed-added-unsorted-duplicate",
    ),
]
# fmt: on


@pytest.mark.parametrize("field_ids, expected_field_names", params)
def test_update_product_type(app, field_ids, expected_field_names):

    with app.app_context():
        count = TypeFieldAssociation.query.count()
        model = ProductType.query.filter_by(type_id=1).one()
        expected_len_change = len(model.fields) - len(expected_field_names)

    with app.app_context():
        model = ops.update_product_type(
            type_id=1,
            name="compass",
            order=5,
            indef_article="a",
            singular="compass",
            plural="compasses",
            icon="mdi-compass",
            field_ids=field_ids,
        )
        ops.commit()

    with app.app_context():
        model = ProductType.query.filter_by(type_id=1).one()
        assert model.name == "compass"
        assert model.order == 5
        assert model.indef_article == "a"
        assert model.singular == "compass"
        assert model.plural == "compasses"
        assert model.icon == "mdi-compass"
        actual_field_names = [f.field.name for f in model.fields]
        assert actual_field_names == expected_field_names

        # assert unused TypeFieldAssociation is deleted
        actual_len_change = count - TypeFieldAssociation.query.count()
        assert expected_len_change == actual_len_change


params = [
    pytest.param([1, 2, 3, 88], id="non-existent"),
]


##__________________________________________________________________||
def test_delete_product_type(app):
    name = "map"

    with app.app_context():
        count = ProductType.query.count()
        model = ProductType.query.filter_by(name=name).one()
        type_id = model.type_id

    with app.app_context():
        model = ops.delete_product_type(type_id=type_id)
        ops.commit()

    with app.app_context():
        model = ProductType.query.filter_by(name=name).one_or_none()
        assert model is None
        assert ProductType.query.count() == (count - 1)


##__________________________________________________________________||
