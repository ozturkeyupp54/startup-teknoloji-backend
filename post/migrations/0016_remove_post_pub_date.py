# Generated by Django 4.2.9 on 2024-02-16 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_alter_post_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
