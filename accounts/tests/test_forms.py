from django.test import TestCase
from accounts.forms import CustomUserCreationForm

class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self):
        data = {'username': 'testuser', 'password1': 'password', 'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'username': '', 'password1': 'password', 'password2': 'password'}
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())
