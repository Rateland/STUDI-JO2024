from django.test import TestCase, Client
from django.urls import reverse

class StoreWorkflowTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_to_cart_workflow(self):
        # Ajout au panier
        response = self.client.post(reverse('add_to_cart'), {'product_id': 1, 'quantity': 1})
        self.assertEqual(response.status_code, 302)  # Redirection après ajout au panier