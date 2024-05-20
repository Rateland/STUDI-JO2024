from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30, blank=True, verbose_name="Nom")
    prenom = models.CharField(max_length=30, blank=True, verbose_name="Prénom")

    def __str__(self):
        return f"{self.prenom} {self.nom}"