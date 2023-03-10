# Generated by Django 4.1.7 on 2023-02-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(max_length=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, unique=True),
        ),
    ]
