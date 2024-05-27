from django.test import TestCase
from accounts.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(username='testuser', password='password')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password'))