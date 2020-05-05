import graphene

##__________________________________________________________________||
class CommonAttribute:
    name = graphene.String()
    contact = graphene.String()
    date_produced = graphene.Date()
    produced_by = graphene.String()
    posted_by = graphene.String()
    updated_by = graphene.String()

##__________________________________________________________________||
