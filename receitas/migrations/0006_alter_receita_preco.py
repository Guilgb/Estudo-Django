# Generated by Django 4.0.6 on 2022-09-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_receita_preco_pedidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]