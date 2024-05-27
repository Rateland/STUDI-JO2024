from django.test import TestCase
from store.forms import ProductForm  # Remplacez 'ProductForm' par vos formulaires réels

class ProductFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test Product', 'price': 10.0}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'price': 10.0}
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())