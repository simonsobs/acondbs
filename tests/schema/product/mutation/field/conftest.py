import pytest

from acondbs.models import FieldType
from acondbs import ops


##__________________________________________________________________||
@pytest.fixture
def app(app_users):
    y = app_users
    with y.app_context():
        # fmt: off
        ops.create_field(field_id=1, name="contact", type_=FieldType.UnicodeText)
        ops.create_field(field_id=2, name="produced_by", type_=FieldType.UnicodeText)
        ops.create_field(field_id=3, name="date_produced", type_=FieldType.Date)
        # fmt: on
        ops.commit()
    yield y


##__________________________________________________________________||
