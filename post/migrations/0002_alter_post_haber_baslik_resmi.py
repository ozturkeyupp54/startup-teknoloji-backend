# Generated by Django 4.2.9 on 2024-02-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='haber_baslik_resmi',
            field=models.ImageField(blank=True, default='/haber_baslik_resmi/turkiye-ve-dunyadaki-en-populer-girisimcilik-zirveleri-StartupTeknoloji-1.jpg', null=True, upload_to='haber_baslik_resmi/'),
        ),
    ]
