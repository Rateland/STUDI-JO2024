# Generated by Django 5.0.3 on 2024-04-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_offrebillet_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='offrebillet',
            name='slug',
            field=models.SlugField(default='', max_length=128),
            preserve_default=False,
        ),
    ]