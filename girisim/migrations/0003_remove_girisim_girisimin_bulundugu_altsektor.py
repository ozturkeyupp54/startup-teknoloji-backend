# Generated by Django 4.2.9 on 2024-02-11 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girisim', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='girisim',
            name='girisimin_bulundugu_altsektor',
        ),
    ]
