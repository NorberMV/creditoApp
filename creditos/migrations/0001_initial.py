# Generated by Django 3.2.6 on 2021-08-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0004_alter_cliente_banco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_credito', models.TextField(blank=True)),
                ('pago_minimo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pago_maximo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('plazo_credito', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('tipo_credito', models.CharField(choices=[('Automotriz', 'Automotriz'), ('Hipotecarios', 'Hipotecarios'), ('Comerciales', 'Comerciales')], max_length=20, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]
