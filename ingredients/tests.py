import json
import unittest

import graphene
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

from .models import Category, Ingredient
from .schema import Query

schema = graphene.Schema(query=Query)


class CategoryModelTestCase(GraphQLTestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_model(self):
        self.assertEqual(str(self.category), self.category.name)


class IngredientModelTestCase(GraphQLTestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.ingredient = Ingredient.objects.create(name="Test Category",
                                                    notes="Test Ingredient", category=self.category)

    def test_ingredient_model(self):
        self.assertEqual(str(self.ingredient), self.ingredient.name)


class BooksTestCase(GraphQLTestCase):
    def setUp(self):
        self.caegory_1 = Category.objects.create(name="Test Category")
        self.caegory_2 = Category.objects.create(name="Second Category")
        self.caegory_3 = Category.objects.create(name="Third Category")

    def test_categories_query(self):
        response = self.query(
            '''
            query {
                allCategories {
                    edges {
                        node {
                            id
                            name
                        }
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['data']['allCategories']['edges']), 3)
        self.assertEqual(content['data']['allCategories']
                         ['edges'][0]['node']['name'], self.caegory_1.name)


class IngredentsTestCase(GraphQLTestCase):
    def setUp(self):
        self.client = Client(schema)
        self.category_1 = Category.objects.create(name="Test Category")
        self.category_2 = Category.objects.create(name="Second Category")
        self.ingredient_1 = Ingredient.objects.create(name="Ingredient 1",
                                                      notes="Test Ingredient", category=self.category_1)
        self.ingredient_2 = Ingredient.objects.create(name="Ingredient 2",
                                                      notes="Test Ingredient 2", category=self.category_2)
        self.ingredient_3 = Ingredient.objects.create(name="Ingredient 3",
                                                      notes="Test Ingredient 3", category=self.category_2)

    @unittest.skip("Unhandled error")
    def test_ingredient_query(self):
        query = '''
            query testQuery($id: ID!) {
                ingredient(id: $id) {
                    name
                }
            }
        '''
        variables = {'id': self.ingredient_1.pk}
        response = self.client.execute(query, variables=variables)
        self.assertEqual(response['data']['name'], self.caegory_1.name)

    def test_ingredients_query(self):
        query = '''
            query {
                allIngredients {
                    edges {
                        node {
                            id
                            name
                            notes
                            category {
                                id
                                name
                            }
                        }
                    }
                }
            }
        '''

        response = self.client.execute(query)
        self.assertEqual(len(response['data']['allIngredients']['edges']), 3)
        self.assertEqual(response['data']['allIngredients']['edges'][1]['node']['name'],
                         self.ingredient_2.name)
        self.assertEqual(response['data']['allIngredients']['edges'][1]['node']['category']['name'],
                         self.category_2.name)
