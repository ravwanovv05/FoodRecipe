# Generated by Django 5.0.1 on 2024-01-27 10:52

import account.models.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.managers.CustomUserManager()),
            ],
        ),
    ]