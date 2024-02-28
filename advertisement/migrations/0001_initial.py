# Generated by Django 5.0.2 on 2024-02-26 15:11

import django.db.models.deletion
import imagekit.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kampanya_creator_adi', models.CharField(max_length=255)),
                ('kampanya_creator_soyadi', models.CharField(max_length=255)),
                ('kampanya_basligi', models.CharField(max_length=255, unique=True)),
                ('sirket_adi', models.CharField(max_length=255)),
                ('kampanya_baslangic_tarihi', models.DateField()),
                ('advertisement_ust_resmi', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='anasayfa_ust_taraf_reklam_resmi/')),
                ('advertisement_alt_resmi', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='anasayfa_alt_taraf_reklam_resmi/')),
                ('kampanyanin_websitesinin_linki', models.URLField()),
                ('advertisement_ust_resmi_views', models.PositiveIntegerField(default=0)),
                ('advertisement_alt_resmi_views', models.PositiveIntegerField(default=0)),
                ('reklam_gosterim_yeri', models.CharField(choices=[('Üst', 'Üst'), ('Alt', 'Alt'), ('Her İkiside', 'Her İkiside')], default='Her İkiside', max_length=15)),
                ('max_views_per_image', models.PositiveIntegerField(blank=True, default=100, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('kampanya_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
                'db_table': 'advertisement',
                'ordering': ['-pk'],
            },
        ),
    ]
