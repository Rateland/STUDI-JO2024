from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from Jeux_Olympiques_France.settings import AUTH_USER_MODEL


# Create your models here.
class Epreuve(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre de l’épreuve")
    slug = models.SlugField(max_length=128)
    type = models.CharField(max_length=128, verbose_name="Type d’épreuve", blank=True, null=True)
    description = models.TextField(verbose_name="Description de l’épreuve")
    mention = models.TextField(verbose_name="Mentions", blank=True, null=True)
    date_epreuve = models.DateField(verbose_name="Date de l’épreuve")
    illustration = models.ImageField(upload_to="imgbank", blank=True, null=True)

    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse("epreuves", kwargs={"slug": self.slug})

class OffreBillet(models.Model):
    TYPE_OFFRE_CHOICES = [
        ('SOLO', 'Solo'),
        ('DUO', 'Duo'),
        ('FAMILLE', 'Famille'),
    ]

    nom = models.CharField(max_length=100, choices=TYPE_OFFRE_CHOICES, unique=True, verbose_name="Type d’offre", null=True, blank=True)
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, verbose_name="Description de l’offre")
    stock = models.IntegerField(default=0)
    prix = models.DecimalField(default=0.0, max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Prix de l’offre")
    nombre_personnes = models.PositiveIntegerField(verbose_name="Nombre de personne par billet")
    epreuve = models.ForeignKey(Epreuve, null=True, related_name='offres', on_delete=models.CASCADE, verbose_name="Épreuve associée")

    def __str__(self):
        return f"Offre {self.get_nom_display()} - {self.prix}€ - {self.stock} de places restantes"
    
    def get_absolute_url(self):
        return reverse("billets", kwargs={"slug": self.slug})

class Panier(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    acheté = models.BooleanField(default=False)
    date_achat = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.utilisateur.username if self.utilisateur else "Panier temporaire"

class Achat(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    billet = models.ForeignKey(OffreBillet, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, null=True, blank=True)  # Associer directement à un panier
    quantité = models.IntegerField(default=1)
    acheté = models.BooleanField(default=False)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.billet.nom} ({self.quantité})"
    
class Transaction(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    panier = models.ForeignKey(Panier, on_delete=models.SET_NULL, null=True, blank=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('reussi', 'Réussi'), ('echoue', 'Échoué')])
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.utilisateur.username} - {self.status}"
    
class Ticket(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    achats = models.ManyToManyField(Achat)
    date_creation = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.utilisateur.username} - {self.montant_total} €"
    
def serialize_ticket(ticket):
    return {
        'transaction_id': ticket.transaction.id,
        'utilisateur': ticket.utilisateur.username,
        'montant_total': str(ticket.montant_total),
        'achats': [
            {
                'billet': achat.billet.nom,
                'quantité': achat.quantité,
                'prix': str(achat.billet.prix)
            }
            for achat in ticket.achats.all()
        ],
        'date_creation': ticket.date_creation.isoformat()
    }