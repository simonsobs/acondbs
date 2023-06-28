import enum

from acondbs.db.sa import sa

from . import attribute


class FieldType(enum.Enum):
    # SQLAlchemy generic types: https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types
    UnicodeText = 1
    Boolean = 2
    Integer = 3
    Float = 4
    Date = 5
    DateTime = 6
    Time = 7

    @property
    def attribute_class(self):
        return FIELDTYPE_ATTRIBUTECLASS_MAP[self]


FIELDTYPE_ATTRIBUTECLASS_MAP = {
    FieldType.UnicodeText: attribute.AttributeUnicodeText,  # type: ignore
    FieldType.Boolean: attribute.AttributeBoolean,  # type: ignore
    FieldType.Integer: attribute.AttributeInteger,  # type: ignore
    FieldType.Float: attribute.AttributeFloat,  # type: ignore
    FieldType.Date: attribute.AttributeDate,  # type: ignore
    FieldType.DateTime: attribute.AttributeDateTime,  # type: ignore
    FieldType.Time: attribute.AttributeTime,  # type: ignore
}


saEnumFieldType = sa.Enum(FieldType)  # to be imported in another module


class Field(sa.Model):  # type: ignore
    __tablename__ = "field"
    field_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.UnicodeText(), nullable=False)
    type_ = sa.Column(saEnumFieldType, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r} {self.type_name!r}>"

    @property
    def type_name(self):
        # used in __repr__()
        try:
            return self.type_.name
        except BaseException:
            return self.type_
