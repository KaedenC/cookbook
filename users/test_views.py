# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User

# class RegisterViewTest(TestCase):
#     def test_register_success(self):
#         # Create a POST request with valid form data
#         response = self.client.post(reverse('user-register'), {
#             'username': 'testuser',
#             'password1': 'testpassword',
#             'password2': 'testpassword'
#         })
        
#         # Check that the user is redirected to the login page
#         self.assertRedirects(response, reverse('user-login'))
        
#         # Check that the user is created in the database
#         self.assertTrue(User.objects.filter(username='testuser').exists())
        
#         # Check that the success message is displayed
#         messages = list(response.context['messages'])
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "testuser, your account is created, please login.")
        
#     def test_register_invalid_form(self):
#         # Create a POST request with invalid form data
#         response = self.client.post(reverse('user-register'), {
#             'username': 'testuser',
#             'password1': 'testpassword',
#             'password2': 'differentpassword'
#         })
        
#         # Check that the user is not created in the database
#         self.assertFalse(User.objects.filter(username='testuser').exists())
        
#         # Check that the form is rendered again with errors
#         self.assertTemplateUsed(response, 'users/register.html')
#         self.assertContains(response, 'Please make sure the passwords match.')