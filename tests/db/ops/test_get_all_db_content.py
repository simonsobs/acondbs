from sqlalchemy import MetaData

import pytest

from acondbs.db.ops import get_all_db_content
from acondbs.db.sa import sa

##__________________________________________________________________||
def test_get_all_db_content(app, snapshot):
    """test get_all_db_content()

    """

    with app.app_context():
        snapshot.assert_match(get_all_db_content())

##__________________________________________________________________||
