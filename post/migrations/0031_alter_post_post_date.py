# Generated by Django 4.2.9 on 2024-02-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0030_remove_post_author_foreign_key_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
