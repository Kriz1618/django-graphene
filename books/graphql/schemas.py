import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .mutations import FileUploadMutation, InsertBookMutation
from .types import BookType


class Mutation(graphene.ObjectType):
    file_upload = FileUploadMutation.Field()
    insert_book = InsertBookMutation.Field()


class Query(graphene.ObjectType):
    book = graphene.relay.Node.Field(BookType)
    all_books = DjangoFilterConnectionField(BookType)
