# Create your tests here.
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .views import register, profile

class RegisterViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.register_url = reverse('user-register')
        
    def test_register_view_get(self):
        request = self.factory.get(self.register_url)
        response = register(request)
        self.assertEqual(response.status_code, 200)
        
def test_register_view_post_valid_form(self):
    data = {
        'username': 'testuser',
        'password1': 'testpassword123',
        'password2': 'testpassword123'
    }
    request = self.factory.post(self.register_url, data)
    response = register(request)
    # Check if the response is a redirect
    self.assertEqual(response.status_code, 302)
    # Check if the redirection URL is correct
    self.assertEqual(response.url, reverse('user-login'))

class ProfileViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.profile_url = reverse('user-profile')
        
    def test_profile_view_authenticated_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        request = self.factory.get(self.profile_url)
        request.user = user
        response = profile(request)
        self.assertEqual(response.status_code, 200)
        
    def test_profile_view_unauthenticated_user(self):
        request = self.factory.get(self.profile_url)
        response = profile(request)
        self.assertEqual(response.status_code, 302)  # Redirects unauthenticated users to login page