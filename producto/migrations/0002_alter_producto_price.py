# Generated by Django 4.2 on 2023-05-07 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
