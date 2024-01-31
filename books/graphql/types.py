import graphene
from graphene_django import DjangoObjectType

from books.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"
        filter_fields = ["title"]
        interfaces = (graphene.relay.Node,)
