from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30, blank=True, verbose_name="Nom")
    prenom = models.CharField(max_length=30, blank=True, verbose_name="Prénom")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone")

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.phone}"