# Generated by Django 4.0.6 on 2022-08-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank='True', upload_to='fotos/%d/%m/%Y'),
        ),
    ]
