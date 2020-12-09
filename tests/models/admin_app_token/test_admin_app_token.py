import pytest

from sqlalchemy import exc

from acondbs.db.sa import sa
from acondbs.models import AdminAppToken

# __________________________________________________________________||
def test_token(app_empty):
    app = app_empty

    token1 = AdminAppToken(token="token123")

    with app.app_context():
        sa.session.add(token1)
        sa.session.commit()

    with app.app_context():
        token1 = AdminAppToken.query.all()
        print(token1[0].token)        
        # assert map1 is not None
        # type_map = map1.type_
        # assert 'map' == type_map.name
        # assert [map1] == type_map.products

# __________________________________________________________________||
