from django.test import TestCase
from store.models import Epreuve, OffreBillet, Panier, Achat
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class EpreuveModelTest(TestCase):
    def test_epreuve_creation(self):
        epreuve = Epreuve.objects.create(
            titre="Test Epreuve",
            slug="test-epreuve",
            description="Description de test"
        )
        self.assertEqual(epreuve.titre, "Test Epreuve")
        self.assertEqual(epreuve.slug, "test-epreuve")

class OffreBilletModelTest(TestCase):
    def test_offre_creation(self):
        epreuve = Epreuve.objects.create(titre="Epreuve Test", slug="epreuve-test")
        offre = OffreBillet.objects.create(
            nom="SOLO",
            slug="solo",
            description="Offre Solo",
            epreuve=epreuve
        )
        self.assertEqual(offre.nom, "SOLO")
        self.assertEqual(offre.epreuve.titre, "Epreuve Test")


class PanierModelTest(TestCase):
    def test_panier_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        panier = Panier.objects.create(utilisateur=user)
        self.assertEqual(panier.utilisateur.username, 'testuser')

    def test_ajouter_achat(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        epreuve = Epreuve.objects.create(titre="Epreuve Test", slug="epreuve-test")
        offre = OffreBillet.objects.create(
            nom="SOLO",
            slug="solo",
            description="Offre Solo",
            epreuve=epreuve
        )
        panier = Panier.objects.create(utilisateur=user)
        achat = Achat.objects.create(
            billet=offre,
            panier=panier,
            quantité=2
        )
        self.assertEqual(panier.achats.count(), 1)
        self.assertEqual(achat.quantité, 2)


class AchatIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_ajout_panier_via_vue(self):
        epreuve = Epreuve.objects.create(titre="Epreuve Test", slug="epreuve-test")
        offre = OffreBillet.objects.create(
            nom="SOLO",
            slug="solo",
            description="Offre Solo",
            epreuve=epreuve
        )
        response = self.client.get(reverse('panier_epreuves', kwargs={'epreuve_slug': 'epreuve-test', 'billet_slug': 'solo'}))
        self.assertEqual(response.status_code, 302)
        panier = Panier.objects.get(utilisateur=self.user)
        self.assertEqual(panier.achats.count(), 1)