import pytest

# from sqlalchemy import exc

from acondbs import ops
from acondbs.ops.product import _normalize_paths
from acondbs.models import Product, GitHubUser


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
# fmt: off
params_paths = [
    pytest.param(None, id="none"),
    pytest.param([], id="empty"),
    pytest.param(["/a/b/c"], id="one"),
    pytest.param(["/d/e", "/a/b/c", "/f/g"], id="multiple"),
    pytest.param(["  /d/e ", " ", "/a/b/c", "/f/g", "/d/e"], id="not-normalized"),
]
# fmt: on


@pytest.mark.parametrize("paths", params_paths)
@pytest.mark.parametrize("user_login", [None, "user1"])
def test_create(app, user_login, paths):

    with app.app_context():
        count = Product.query.count()

    with app.app_context():
        kwargs = {"type_id": 1, "name": "new-product"}

        if user_login:
            user1 = GitHubUser.query.filter_by(login=user_login).one()
            kwargs["user"] = user1

        if paths is not None:
            kwargs["paths"] = paths

        model = ops.create_product(**kwargs)
        assert model.name == "new-product"
        ops.commit()
        product_id = model.product_id
        assert product_id

    with app.app_context():
        assert Product.query.count() == (count + 1)

    with app.app_context():
        model = Product.query.filter_by(product_id=product_id).one()
        assert model.name == "new-product"

        if user_login:
            assert model.posting_git_hub_user.login == "user1"
        else:
            assert model.posting_git_hub_user is None

        if paths is not None:
            expected = _normalize_paths(paths)
            actual = [p.path for p in model.paths]
            assert actual == expected
        else:
            assert model.paths == []
