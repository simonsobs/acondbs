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
