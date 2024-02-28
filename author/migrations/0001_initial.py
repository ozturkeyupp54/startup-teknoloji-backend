# Generated by Django 4.2.9 on 2024-02-11 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.ImageField(default='', upload_to='profile_pictures/')),
                ('bio', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=800)])),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Yazar',
                'verbose_name_plural': 'Yazarlar',
                'db_table': 'author',
                'ordering': ['-pk'],
            },
        ),
    ]
