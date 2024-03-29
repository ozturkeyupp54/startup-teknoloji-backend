# Generated by Django 4.2.9 on 2024-02-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_remove_post_status_post_publish_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='p', max_length=100),
        ),
    ]
