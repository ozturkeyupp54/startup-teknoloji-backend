# Generated by Django 5.0.2 on 2024-02-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_remove_advertisement_advertisement_alt_resmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='reklam_gosterim_yeri',
            field=models.CharField(default='Üst', max_length=15),
        ),
    ]