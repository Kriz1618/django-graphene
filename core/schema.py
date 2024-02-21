import graphene
from graphene.types import ObjectType, ResolveInfo
from graphene_django import DjangoObjectType

import books.graphql.schemas as books_schema
import ingredients.schema
import users.graphql.schemas as users_schema
from books.models import Book
from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
        interfaces = (graphene.relay.Node,)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "created_at", "updated_at")


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self: "CreateBookMutation", info: ResolveInfo, title: str, description: str) -> "CreateBookMutation":
        book = Book(title=title, description=description)
        book.save()
        return CreateBookMutation(book=book)


class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)  # noqa: A002

    message = graphene.String()

    def mutate(self: "DeleteBookMutation", info: ResolveInfo, id: str) -> "DeleteBookMutation":  # noqa: A002
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBookMutation(message="Book deleted")


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    book = graphene.Field(BookType)

    def mutate(
        self: "UpdateBookMutation", info: ResolveInfo, id: str, title: str, description: str  # noqa: A002
    ) -> "UpdateBookMutation":
        book = Book.objects.get(pk=id)
        book.title = title
        book.description = description
        book.save()
        return UpdateBookMutation(book=book)


class Query(ingredients.schema.Query, books_schema.Query, users_schema.Query, graphene.ObjectType):
    ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_ingredients(root: ObjectType, info: ResolveInfo) -> list[Ingredient]:
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root: ObjectType, info: ResolveInfo, name: str) -> Category:
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class Mutation(books_schema.Mutation, users_schema.Mutation, graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
