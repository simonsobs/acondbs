import graphene

##__________________________________________________________________||
class CommonProductInputFields:
    """Common input fields of mutations for creating and updating different kinds of products

    """
    contact = graphene.String()
    note = graphene.String()

class CommonCreateProductInputFields(CommonProductInputFields):
    """Common input fields of mutations for creating different kinds of products

    """
    name = graphene.String(required=True)
    date_produced = graphene.Date()
    produced_by = graphene.String()
    posted_by = graphene.String()

class CommonUpdateProductInputFields(CommonProductInputFields):
    """Common input fields of mutations for updating different kinds of products

    """
    updated_by = graphene.String()

##__________________________________________________________________||
