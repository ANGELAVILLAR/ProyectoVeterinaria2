# Generated by Django 4.2 on 2023-05-07 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0004_categoria_remove_articulo_category_articulo_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='description',
        ),
    ]
