from ...db.sa import sa


##__________________________________________________________________||
class AttributeBase:
    attribute_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"


##__________________________________________________________________||
class AttributeText(sa.Model, AttributeBase):
    __tablename__ = "attribute_text"
    product_id = sa.Column(
        sa.Integer(), sa.ForeignKey("products.product_id"), nullable=False
    )
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_text", cascade="all, delete-orphan"),
    )
    value = sa.Column(sa.Text())


class AttributeDate(sa.Model, AttributeBase):
    __tablename__ = "attribute_date"
    product_id = sa.Column(
        sa.Integer(), sa.ForeignKey("products.product_id"), nullable=False
    )
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_date", cascade="all, delete-orphan"),
    )
    value = sa.Column(sa.Date())


class AttributeDateTime(sa.Model, AttributeBase):
    __tablename__ = "attribute_date_time"
    product_id = sa.Column(
        sa.Integer(), sa.ForeignKey("products.product_id"), nullable=False
    )
    product = sa.relationship(
        "Product",
        backref=sa.backref("attributes_date_time", cascade="all, delete-orphan"),
    )
    value = sa.Column(sa.DateTime())

##__________________________________________________________________||
