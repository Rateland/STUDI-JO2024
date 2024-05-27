from django.test import TestCase, Client
from django.urls import reverse

class AccountsWorkflowTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_and_login(self):
        # Inscription
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 302)  # Redirection après inscription réussie

        # Connexion
        response = self.client.post(reverse('login'), {'username': 'newuser', 'password': 'password'})
        self.assertEqual(response.status_code, 302)  # Redirection après connexion réussie