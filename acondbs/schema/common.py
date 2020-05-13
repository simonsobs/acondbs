import graphene

##__________________________________________________________________||
class CommonProductInputFields:
    """Common input fields of mutations for creating and updating different kinds of objects

    """
    contact = graphene.String()
    note = graphene.String()

class CommonCreateProductInputFields(CommonProductInputFields):
    """Common input fields of mutations for creating different kinds of objects

    """
    name = graphene.String(required=True)
    date_produced = graphene.Date()
    produced_by = graphene.String()
    posted_by = graphene.String()

class CommonUpdateProductInputFields(CommonProductInputFields):
    """Common input fields of mutations for updating different kinds of objects

    """
    updated_by = graphene.String()

##__________________________________________________________________||
