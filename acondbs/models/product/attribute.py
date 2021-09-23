from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import declarative_mixin

from ...db.sa import sa


##__________________________________________________________________||
@declarative_mixin
class AttributeBase:
    attribute_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text())  # TODO: Remove

    @declared_attr
    def product_id(self):
        return sa.Column(sa.Integer(), sa.ForeignKey("products.product_id"), nullable=False)  # fmt: skip

    @declared_attr
    def field_id(self):
        return sa.Column(sa.Integer(), sa.ForeignKey("field.field_id"), nullable=False)  # fmt: skip

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}: {self.value!r}>"


##__________________________________________________________________||
class AttributeUnicodeText(AttributeBase, sa.Model):
    __tablename__ = "attribute_unicode_text"
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_unicode_text", cascade="all, delete-orphan"),  # fmt: skip
    )
    field = sa.relationship(
        "Field",
        backref=sa.backref("attributes_unicode_text", cascade="all, delete-orphan"),  # fmt: skip
    )
    value = sa.Column(sa.UnicodeText())


class AttributeDate(AttributeBase, sa.Model):
    __tablename__ = "attribute_date"
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_date", cascade="all, delete-orphan"),  # fmt: skip
    )
    field = sa.relationship(
        "Field",
        backref=sa.backref("attributes_date", cascade="all, delete-orphan"),  # fmt: skip
    )
    value = sa.Column(sa.Date())


class AttributeDateTime(AttributeBase, sa.Model):
    __tablename__ = "attribute_date_time"
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_date_time", cascade="all, delete-orphan"),  # fmt: skip
    )
    field = sa.relationship(
        "Field",
        backref=sa.backref("attributes_date_time", cascade="all, delete-orphan"),  # fmt: skip
    )
    value = sa.Column(sa.DateTime())


##__________________________________________________________________||
