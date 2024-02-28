# Generated by Django 4.2.9 on 2024-02-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0003_rename_category_industrycategory_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industrysubcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='industrysubcategory',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='industrysubcategory',
            name='subcategory_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='industrycategory',
            name='category_name',
            field=models.CharField(max_length=255),
        ),
    ]