from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from Jeux_Olympiques_France.settings import AUTH_USER_MODEL


# Create your models here.

class Epreuve(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre de l’épreuve")
    slug = models.SlugField(max_length=128)
    description = models.TextField(verbose_name="Description de l’épreuve")
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
    
class Achat(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    billet = models.ForeignKey(OffreBillet, on_delete=models.CASCADE)
    quantité = models.IntegerField(default=1)
    acheté = models.BooleanField(default=False)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.billet.nom} ({self.quantité})"
    
class Panier(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    achats = models.ManyToManyField(Achat)
    acheté = models.BooleanField(default=False)
    date_achat = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        self.utilisateur.username if self.utilisateur else "Panier temporaire"