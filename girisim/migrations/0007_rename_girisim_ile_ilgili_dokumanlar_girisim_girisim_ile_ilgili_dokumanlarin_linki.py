# Generated by Django 4.2.9 on 2024-02-15 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('girisim', '0006_alter_girisim_ekip_arkadasi_telefonu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='girisim',
            old_name='girisim_ile_ilgili_dokumanlar',
            new_name='girisim_ile_ilgili_dokumanlarin_linki',
        ),
    ]
