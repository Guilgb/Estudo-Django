# Generated by Django 4.0.6 on 2022-09-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='adm',
            field=models.BooleanField(default=False),
        ),
    ]