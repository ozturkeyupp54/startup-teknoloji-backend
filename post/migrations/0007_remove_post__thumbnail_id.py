# Generated by Django 4.2.9 on 2024-02-15 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='_thumbnail_id',
        ),
    ]
