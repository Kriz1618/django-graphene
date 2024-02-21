import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .mutations import CreateUserMutation, DeleteUserMutation, UpdateUserMutation
from .types import UserType


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()


class Query(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)
