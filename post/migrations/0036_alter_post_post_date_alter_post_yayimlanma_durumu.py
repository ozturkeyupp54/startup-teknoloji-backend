# Generated by Django 4.2.9 on 2024-02-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0035_remove_post_publish_status_post_yayimlanma_durumu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='yayimlanma_durumu',
            field=models.CharField(choices=[('Taslak', 'Taslak'), ('Yayinda', 'Yayinda')], default='Taslak', max_length=10),
        ),
    ]
