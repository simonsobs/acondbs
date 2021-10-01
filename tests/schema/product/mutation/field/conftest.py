import pytest

from acondbs.models import FieldType
from acondbs import ops


##__________________________________________________________________||
@pytest.fixture
def app(app_users):
    y = app_users
    with y.app_context():
        ops.create_field(name="contact", type_=FieldType.UnicodeText)
        ops.create_field(name="produced_by", type_=FieldType.UnicodeText)
        ops.create_field(name="date_produced", type_=FieldType.Date)
        ops.commit()
    yield y


##__________________________________________________________________||
