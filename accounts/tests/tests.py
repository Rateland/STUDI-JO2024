from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser
from store.models import Panier

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))

    def test_user_is_staff(self):
        staff_user = CustomUser.objects.create_user(username='staffuser', password='testpassword', is_staff=True)
        self.assertTrue(staff_user.is_staff)


class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('accueil'))


class AccountIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_ajout_achat_avec_auth(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('voir_panier'))
        self.assertEqual(response.status_code, 200)