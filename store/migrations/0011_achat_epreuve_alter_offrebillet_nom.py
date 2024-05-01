# Generated by Django 5.0.3 on 2024-04-30 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_offrebillet_epreuve'),
    ]

    operations = [
        migrations.AddField(
            model_name='achat',
            name='epreuve',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.epreuve'),
        ),
        migrations.AlterField(
            model_name='offrebillet',
            name='nom',
            field=models.CharField(blank=True, choices=[('SOLO', 'Solo'), ('DUO', 'Duo'), ('FAMILLE', 'Famille')], max_length=100, null=True, unique=True, verbose_name='Type d’offre'),
        ),
    ]
