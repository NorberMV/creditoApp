# Generated by Django 3.2.6 on 2021-08-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20210810_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]