# Generated by Django 5.1.1 on 2024-11-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saude', '0003_doencasbairro_locais_doencas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locais_doencas',
            old_name='deonca_bairro',
            new_name='doenca_bairro',
        ),
    ]
