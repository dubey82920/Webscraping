# Generated by Django 4.1.3 on 2023-03-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reviews',
            field=models.FloatField(),
        ),
    ]
