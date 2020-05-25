from ..db.sa import sa

##__________________________________________________________________||
class ProductRelationType(sa.Model):
    __tablename__ = 'product_relation_types'
    type_id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.Text(), nullable=False, unique=True, index=True)
    reverse_type_id = sa.Column(sa.ForeignKey('product_relation_types.type_id'))
    reverse = sa.relationship(
        lambda: ProductRelationType,
        uselist=False,
        foreign_keys=[reverse_type_id],
        remote_side="ProductRelationType.type_id",
        cascade="all",
        post_update=True)

##__________________________________________________________________||
