# Generated by Django 5.0.6 on 2024-05-22 15:13

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, verbose_name='Titre de l’épreuve')),
                ('slug', models.SlugField(max_length=128)),
                ('type', models.CharField(blank=True, max_length=128, null=True, verbose_name='Type d’épreuve')),
                ('description', models.TextField(verbose_name='Description de l’épreuve')),
                ('mention', models.TextField(blank=True, null=True, verbose_name='Mentions')),
                ('date_epreuve', models.DateField(verbose_name='Date de l’épreuve')),
                ('illustration', models.ImageField(blank=True, null=True, upload_to='imgbank')),
            ],
        ),
        migrations.CreateModel(
            name='OffreBillet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, choices=[('SOLO', 'Solo'), ('DUO', 'Duo'), ('FAMILLE', 'Famille')], max_length=100, null=True, unique=True, verbose_name='Type d’offre')),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField(blank=True, verbose_name='Description de l’offre')),
                ('stock', models.IntegerField(default=0)),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Prix de l’offre')),
                ('nombre_personnes', models.PositiveIntegerField(verbose_name='Nombre de personne par billet')),
                ('epreuve', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offres', to='store.epreuve', verbose_name='Épreuve associée')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acheté', models.BooleanField(default=False)),
                ('date_achat', models.DateTimeField(blank=True, null=True)),
                ('utilisateur', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantité', models.IntegerField(default=1)),
                ('acheté', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('epreuve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.epreuve')),
                ('billet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offrebillet')),
                ('panier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achats', to='store.panier')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('reussi', 'Réussi'), ('echoue', 'Échoué')], max_length=20)),
                ('date_transaction', models.DateTimeField(auto_now_add=True)),
                ('panier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.panier')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('achats', models.ManyToManyField(to='store.achat')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.transaction')),
            ],
        ),
    ]
