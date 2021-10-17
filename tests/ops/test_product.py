import datetime
import pytest

# from sqlalchemy import exc

from acondbs import ops
from acondbs.ops.product import _normalize_paths
from acondbs.models import Product, FieldType, GitHubUser


##__________________________________________________________________||
# fmt: off
params = [
    pytest.param([], [], id="empty"),
    pytest.param(["/a/b/c"], ["/a/b/c"], id="one"),
    pytest.param([" /a/b/c  "], ["/a/b/c"], id="unstripped"),
    pytest.param(["/d/e", "/a/b/c", "/f/g"], ["/d/e", "/a/b/c", "/f/g"], id="multiple"),
    pytest.param(["/a/b/c", "", "/f/g"], ["/a/b/c", "/f/g"], id="empty-member"),
    pytest.param(["/a/b/c", "  ", "/f/g"], ["/a/b/c", "/f/g"], id="empty-unstripped-member"),
    pytest.param(["/d/e", "/a/b/c", "/d/e"], ["/d/e", "/a/b/c"], id="duplicate"),
    pytest.param(["  /d/e ", "/a/b/c", "/d/e"], ["/d/e", "/a/b/c"], id="duplicate-unstripped"),
]
# fmt: on


@pytest.mark.parametrize("paths, ret", params)
def test_normalize_paths(paths, ret):
    assert _normalize_paths(paths) == ret


##__________________________________________________________________||
params = [
    pytest.param(None, id="none"),
    pytest.param({}, id="empty"),
    pytest.param({1: "An attribute"}, id="one"),
    pytest.param({1: "An attribute", 3: False}, id="two"),
    pytest.param(
        {
            1: "An attribute",
            3: False,
            4: True,
            5: 512,
            6: 2.34,
            8: datetime.datetime(2021, 10, 15, 16, 55, 21),
        },
        id="all",
    ),
]


@pytest.mark.parametrize("attributes", params)
def test_create_attributes(app, attributes):
    return _test_create(app, attributes=attributes)


params = [
    pytest.param(None, id="none"),
    pytest.param([], id="empty"),
    pytest.param([{"type_id": 1, "product_id": 2}], id="one"),
    pytest.param(
        [{"type_id": 2, "product_id": 1}, {"type_id": 1, "product_id": 3}],
        id="multiple",
    ),
]


@pytest.mark.parametrize("relations", params)
def test_create_relations(app, relations):
    return _test_create(app, relations=relations)


params = [
    pytest.param(None, id="none"),
    pytest.param([], id="empty"),
    pytest.param(["/a/b/c"], id="one"),
    pytest.param(["/d/e", "/a/b/c", "/f/g"], id="multiple"),
    pytest.param(
        ["  /d/e ", " ", "/a/b/c", "/f/g", "/d/e"], id="not-normalized"
    ),
]


@pytest.mark.parametrize("paths", params)
def test_create_paths(app, paths):
    return _test_create(app, paths=paths)


@pytest.mark.parametrize("posting_git_hub_user_id", [None, 1])
def test_create_user(app, posting_git_hub_user_id):
    return _test_create(app, posting_git_hub_user_id=posting_git_hub_user_id)


def _test_create(
    app,
    paths=None,
    relations=None,
    attributes=None,
    posting_git_hub_user_id=None,
):

    kwargs = {"type_id": 1, "name": "new-product"}

    if paths is not None:
        kwargs["paths"] = paths

    if relations is not None:
        kwargs["relations"] = relations

    if attributes is not None:
        kwargs["attributes"] = attributes

    if posting_git_hub_user_id:
        kwargs["posting_git_hub_user_id"] = posting_git_hub_user_id

    with app.app_context():
        count = Product.query.count()

        model = ops.create_product(**kwargs)
        assert model.name == "new-product"
        ops.commit()
        product_id = model.product_id
        assert product_id

    with app.app_context():
        assert Product.query.count() == (count + 1)

        model = Product.query.filter_by(product_id=product_id).one()
        assert model.name == "new-product"

        if posting_git_hub_user_id:
            posting_git_hub_user = GitHubUser.query.filter_by(
                user_id=posting_git_hub_user_id
            ).one()
            assert model.posting_git_hub_user == posting_git_hub_user
        else:
            assert model.posting_git_hub_user is None

        if paths is not None:
            expected = _normalize_paths(paths)
            actual = [p.path for p in model.paths]
            assert actual == expected
        else:
            assert model.paths == []

        if relations is not None:
            expected = [(r["type_id"], r["product_id"]) for r in relations]
            actual = [(r.type_id, r.other_product_id) for r in model.relations]
            assert actual == expected
        else:
            assert model.relations == []

        if attributes is None:
            attributes = {}
        expected_field_ids = [f.field_id for f in model.type_.fields]
        expected = {i: attributes.get(i) for i in expected_field_ids}
        actual = _extract_attributes(model)
        actual_field_ids = list(actual.keys())
        assert actual_field_ids == expected_field_ids
        assert actual == expected


##__________________________________________________________________||
def _extract_attributes(model):
    attr_names = [
        a.attribute_class.backref_column
        for a in FieldType.__members__.values()
    ]
    # e.g., 'attributes_unicode_text', 'attributes_boolean'

    attrs = [e for attr in attr_names for e in getattr(model, attr)]
    # e.g., AttributeUnicodeText

    ret = {a.field_id: a.value for a in attrs}

    return ret


##__________________________________________________________________||
params = [
    pytest.param(None, id="none"),
    pytest.param({}, id="empty"),
    pytest.param({1: "An attribute"}, id="one"),
    pytest.param({1: "An attribute", 3: False}, id="two"),
    pytest.param(
        {
            1: "An attribute",
            3: False,
            4: True,
            5: 512,
            6: 2.34,
            8: datetime.datetime(2021, 10, 15, 16, 55, 21),
        },
        id="all",
    ),
]


@pytest.mark.parametrize("attributes", params)
def test_update_attributes(app, attributes):
    return _test_update(app, attributes=attributes)


params = [
    pytest.param(None, id="none"),
    pytest.param([], id="empty"),
    pytest.param(
        [
            {"type_id": 2, "product_id": 3},
            {"type_id": 1, "product_id": 5},
        ],
        id="same",
    ),
    pytest.param(
        [
            {"type_id": 1, "product_id": 5},
        ],
        id="remove",
    ),
    pytest.param(
        [
            {"type_id": 2, "product_id": 3},
            {"type_id": 1, "product_id": 5},
            {"type_id": 1, "product_id": 4},
        ],
        id="add",
    ),
    pytest.param(
        [
            {"type_id": 1, "product_id": 4},
            {"type_id": 2, "product_id": 3},
        ],
        id="add-remove",
    ),
    pytest.param(
        [
            {"type_id": 1, "product_id": 4},
            {"type_id": 2, "product_id": 6},
        ],
        id="replace",
    ),
]


@pytest.mark.parametrize("relations", params)
def test_update_relations(app, relations):
    return _test_update(app, relations=relations)


params = [
    pytest.param(None, id="none"),
    pytest.param([], id="empty"),
    pytest.param(["/d/e", "/a/b/c"], id="same"),
    pytest.param(["/a/b/c", "/d/e"], id="same-perm"),
    pytest.param(["/a/b/c"], id="remove"),
    pytest.param(["/d/e", "/a/b/c", "/f/g"], id="add"),
    pytest.param(["/d/e", "/f/g", "/a/b/c"], id="add-perm"),
    pytest.param(
        ["  /d/e ", " ", "/a/b/c", "/f/g", "/d/e"], id="not-normalized"
    ),
]


@pytest.mark.parametrize("paths", params)
def test_update_paths(app, paths):
    return _test_update(app, paths=paths)


@pytest.mark.parametrize("updating_git_hub_user_id", [None, 2])
def test_update_user(app, updating_git_hub_user_id):
    return _test_update(app, updating_git_hub_user_id=updating_git_hub_user_id)


def _test_update(
    app,
    paths=None,
    relations=None,
    attributes=None,
    updating_git_hub_user_id=None,
):

    product_id = 1
    kwargs = {"product_id": product_id, "name": "new-name"}

    if paths is not None:
        kwargs["paths"] = paths

    if relations is not None:
        kwargs["relations"] = relations

    if attributes is not None:
        kwargs["attributes"] = attributes

    if updating_git_hub_user_id:
        kwargs["updating_git_hub_user_id"] = updating_git_hub_user_id

    with app.app_context():
        count = Product.query.count()

        model = Product.query.filter_by(product_id=product_id).one()
        paths_old = [p.path for p in model.paths]
        path_ids_old = {p.path: p.path_id for p in model.paths}

        relations_old = {
            (r.type_id, r.other_product_id) for r in model.relations
        }
        relation_ids_old = {
            (r.type_id, r.other_product_id): r.relation_id
            for r in model.relations
        }

        attributes_old = _extract_attributes(model)

        model = ops.update_product(**kwargs)
        assert model.name == "new-name"
        ops.commit()

    with app.app_context():
        assert Product.query.count() == count

        model = Product.query.filter_by(product_id=product_id).one()
        assert model.name == "new-name"

        if updating_git_hub_user_id:
            updating_git_hub_user = GitHubUser.query.filter_by(
                user_id=updating_git_hub_user_id
            ).one()
            assert model.updating_git_hub_user == updating_git_hub_user
        else:
            assert model.updating_git_hub_user is None

        # NOTE: The order of the paths is being tested. However, it is
        # probably not possible to control the order. The order in a
        # Python list is not preserved once committed in the DB.
        if paths is not None:
            kept = [p for p in paths_old if p in paths]
            expected = kept + _normalize_paths(paths)
            expected = list(dict.fromkeys(expected))  # uniq order preserved
        else:
            expected = paths_old
        actual = [p.path for p in model.paths]
        assert actual == expected
        expected_path_ids = {
            k: v for k, v in path_ids_old.items() if k in expected
        }
        path_ids = {
            p.path: p.path_id for p in model.paths if p.path in path_ids_old
        }
        assert path_ids == expected_path_ids

        if relations is not None:
            expected = {(r["type_id"], r["product_id"]) for r in relations}
        else:
            expected = relations_old
        actual = {(r.type_id, r.other_product_id) for r in model.relations}
        assert actual == expected
        expected_relation_ids = {
            k: v for k, v in relation_ids_old.items() if k in expected
        }
        relation_ids = {
            (r.type_id, r.other_product_id): r.relation_id
            for r in model.relations
            if (r.type_id, r.other_product_id) in relation_ids_old
        }
        assert relation_ids == expected_relation_ids

        if attributes is None:
            attributes = {}
        expected = attributes_old.copy()
        expected.update(attributes)
        actual = _extract_attributes(model)
        assert actual == expected


##__________________________________________________________________||
def test_delete(app):

    with app.app_context():
        model = ops.create_product(type_id=1, name="to_be_deleted")
        ops.commit()
        product_id = model.product_id

    with app.app_context():
        count = Product.query.count()
        model = ops.delete_product(product_id=product_id)
        ops.commit()

    with app.app_context():
        model = Product.query.filter_by(product_id=product_id).one_or_none()
        assert model is None
        assert Product.query.count() == (count - 1)


##__________________________________________________________________||
