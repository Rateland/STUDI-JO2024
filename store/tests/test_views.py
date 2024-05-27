from django.urls import reverse
from django.test import TestCase, Client

class StoreViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))  # Assurez-vous que 'product_list' est une vue valide
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Produits")
