import graphene
from graphene import Schema

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, World!")

schema = Schema(query=Query)