import graphene
from django.core.files import File
from django.core.files.storage import default_storage
from graphene import ResolveInfo
from graphene_file_upload.scalars import Upload

from books.graphql.types import BookType
from books.models import Book


class FileUploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)
        title = graphene.String()

    success = graphene.Boolean()

    def mutate(self: "FileUploadMutation", info: ResolveInfo, file: Upload, **kwargs: dict) -> "FileUploadMutation":
        default_storage.save(file.name, file)
        return FileUploadMutation(success=True)


class InsertBookMutation(graphene.Mutation):
    class Arguments:
        file = Upload()
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(
        self: "InsertBookMutation", info: ResolveInfo, file: Upload, title: str, description: str
    ) -> "InsertBookMutation":
        book = Book(title=title, description=description)
        if file:
            book.image.save(file.name, File(file), save=False)
        book.save()
        return InsertBookMutation(book=book)
