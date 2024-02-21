from django.contrib.auth.models import User
from graphene_django_cud.mutations import (
    DjangoCreateMutation,
    DjangoDeleteMutation,
    DjangoPatchMutation,
)

from .types import UserType


class CreateUserMutation(DjangoCreateMutation):
    class Meta:
        model = User


class UpdateUserMutation(DjangoPatchMutation):
    class Meta:
        model = User


class DeleteUserMutation(DjangoDeleteMutation):
    class Meta:
        model = User
