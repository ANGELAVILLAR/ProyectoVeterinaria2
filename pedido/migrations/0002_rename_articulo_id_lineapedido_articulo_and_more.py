# Generated by Django 4.2 on 2023-05-11 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='articulo_id',
            new_name='articulo',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
    ]