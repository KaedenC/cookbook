from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.recipe = Recipe.objects.create(title='Test Recipe', description='Test Description', author=self.user)

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/home.html')
        self.assertIn(self.recipe, response.context['object_list'])

    def test_about_view(self):
        response = self.client.get(reverse('recipes-about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/about.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes-detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')
        self.assertEqual(response.context['object'], self.recipe)

    def test_recipe_create_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('recipes-create'), {'title': 'New Recipe', 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Recipe.objects.filter(title='New Recipe').exists())

    def test_recipe_update_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('recipes-update', kwargs={'pk': self.recipe.pk}), {'title': 'Updated Recipe', 'description': 'Updated Description'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'Updated Recipe')

    def test_recipe_delete_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('recipes-delete', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(Recipe.objects.filter(title='Test Recipe').exists())
