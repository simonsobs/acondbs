import enum

from ...db.sa import sa


##__________________________________________________________________||
class FieldType(enum.Enum):
    # SQLAlchemy generic types: https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types
    UnicodeText = 1
    Boolean = 2
    Integer = 3
    Float = 4
    Date = 5
    DateTime = 6
    Time = 7


saEnumFieldType = sa.Enum(FieldType)  # to be imported in another module


class Field(sa.Model):
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


class TypeFieldAssociation(sa.Model):
    __tablename__ = "type_field_association"
    type_id = sa.Column(
        #
        sa.Integer(),
        sa.ForeignKey("product_types.type_id"),
        primary_key=True,
    )
    field_id = sa.Column(
        #
        sa.Integer(),
        sa.ForeignKey("field.field_id"),
        primary_key=True,
    )
    type_ = sa.relationship(
        "ProductType",
        backref=sa.backref("fields", cascade="all, delete-orphan"),
    )
    field = sa.relationship(
        "Field",
        backref=sa.backref("entry_types", cascade="all, delete-orphan"),
    )

    def __repr__(self):
        type_name = self.type_.name if self.type_ else self.type_
        field_name = self.field.name if self.field else self.field
        return f"<{self.__class__.__name__} {type_name!r} {field_name!r}>"


##__________________________________________________________________||
