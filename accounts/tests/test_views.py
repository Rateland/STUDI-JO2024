from django.urls import reverse
from django.test import TestCase, Client

class AccountsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Connexion")