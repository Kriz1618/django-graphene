import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        filter_fields = ["username", "first_name", "last_name", "email"]
        interfaces = (graphene.relay.Node,)
