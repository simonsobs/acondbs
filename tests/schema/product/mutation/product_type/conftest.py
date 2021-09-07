import pytest

import datetime

from acondbs import create_app
from acondbs.db.ops import define_tables

from acondbs.db.sa import sa
from acondbs.models import GitHubToken, GitHubUser, AccountAdmin
from acondbs.models import ProductType, Product


##__________________________________________________________________||
@pytest.fixture
def app_empty():
    database_uri = "sqlite:///:memory:"
    y = create_app(SQLALCHEMY_DATABASE_URI=database_uri)
    with y.app_context():
        define_tables()
    yield y


@pytest.fixture
def app_users(app_empty):
    y = app_empty

    # user1: octocat - admin
    user1 = GitHubUser(login="octocat", git_hub_id="04:User583231")
    token1 = GitHubToken(  # noqa: F841
        token="90b2ee5fed25506df04fd37343bb68d1803dd97f", scope="", user=user1
    )
    admin1 = AccountAdmin(git_hub_login="octocat")

    # user2: dojocat - not admin
    user2 = GitHubUser(login="dojocat", git_hub_id="04:User9758946")
    token2 = GitHubToken(  # noqa: F841
        token="0fb8c9e16d6f7c4961c4c49212bf197d79f14080", scope="", user=user2
    )

    with y.app_context():
        sa.session.add(user1)
        sa.session.add(admin1)
        sa.session.add(user2)
        sa.session.commit()
    yield y


@pytest.fixture
def app(app_users):

    y = app_users

    # create product types
    Map = ProductType(
        type_id=1,
        name="map",
        order=2,
        indef_article="a",
        singular="map",
        plural="maps",
        icon="mdi-map",
    )
    Beam = ProductType(
        type_id=2,
        name="beam",
        order=1,
        indef_article="a",
        singular="beam",
        plural="beams",
        icon="mdi-spotlight-beam",
    )

    # create products
    map1 = Product(  # noqa: F841
        name="map1", date_produced=datetime.date(2020, 2, 1), type_=Map
    )
    map2 = Product(  # noqa: F841
        name="map2", date_produced=datetime.date(2020, 5, 10), type_=Map
    )
    map3 = Product(  # noqa: F841
        name="map3", date_produced=datetime.date(2020, 3, 3), type_=Map
    )

    with y.app_context():
        sa.session.add(Map)
        sa.session.add(Beam)
        sa.session.commit()
    yield y


##__________________________________________________________________||
