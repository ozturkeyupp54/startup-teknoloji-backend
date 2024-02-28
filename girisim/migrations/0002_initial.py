# Generated by Django 4.2.9 on 2024-02-11 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investor', '0001_initial'),
        ('girisim', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='girisiminyatirimturlari',
            name='girisimci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='girisiminyatirimturlari',
            name='yatirimin_ilgili_oldugu_girisim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girisim.girisim'),
        ),
        migrations.AddField(
            model_name='girisimhaberleri',
            name='girisimci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='girisimhaberleri',
            name='haberin_ilgili_oldugu_girisim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girisim.girisim'),
        ),
        migrations.AddField(
            model_name='girisimgelismelerhedefler',
            name='girisimci',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='girisimgelismelerhedefler',
            name='target_to_girisim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='girisim.girisim'),
        ),
        migrations.AddField(
            model_name='girisim',
            name='girisimci',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='girisim',
            name='girisimin_bulundugu_altsektor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='investor.industrysubcategory'),
        ),
        migrations.AddField(
            model_name='girisim',
            name='girisimin_bulundugu_sektor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='investor.industrycategory'),
        ),
    ]