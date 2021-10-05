from ...db.sa import sa


##__________________________________________________________________||
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
