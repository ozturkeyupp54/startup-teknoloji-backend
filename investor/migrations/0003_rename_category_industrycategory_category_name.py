# Generated by Django 4.2.9 on 2024-02-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industrycategory',
            old_name='category',
            new_name='category_name',
        ),
    ]
