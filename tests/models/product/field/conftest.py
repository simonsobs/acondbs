import pytest

from acondbs.db.sa import sa
from acondbs.models import FieldType, Field


##__________________________________________________________________||
@pytest.fixture
def app(app_empty):

    y = app_empty

    field1 = Field(name="field1", type_=FieldType.UnicodeText)
    field2 = Field(name="field2", type_=FieldType.Boolean)
    field3 = Field(name="field3", type_=FieldType.Integer)
    field4 = Field(name="field4", type_=FieldType.Float)
    field5 = Field(name="field5", type_=FieldType.Date)
    field6 = Field(name="field6", type_=FieldType.DateTime)
    field7 = Field(name="field7", type_=FieldType.Time)

    fieldu = Field(name="フィールド", type_=FieldType.UnicodeText)

    with y.app_context():
        sa.session.add(field1)
        sa.session.add(field2)
        sa.session.add(field3)
        sa.session.add(field4)
        sa.session.add(field5)
        sa.session.add(field6)
        sa.session.add(field7)
        sa.session.add(fieldu)
        sa.session.commit()

    yield y


##__________________________________________________________________||
