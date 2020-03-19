# Generated by Django 2.0 on 2020-03-19 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('empresa', models.CharField(max_length=255, verbose_name='Empresa')),
                ('latitud', models.FloatField(verbose_name='Latitud')),
                ('longitud', models.FloatField(verbose_name='Longitud')),
                ('pais', django_countries.fields.CountryField(max_length=2)),
                ('estado', models.CharField(choices=[('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chihuahua', 'Chihuahua'), ('Chiapas', 'Chiapas'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('CDMX', 'Ciudad de México'), ('Durango', 'Durango'), ('Guerrero', 'Guerrero'), ('Guanajuato', 'Guanajuato'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('Sinaloa', 'Sinaloa'), ('San Luis Potosí', 'San Luis Potosí'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], max_length=255, verbose_name='Estado')),
                ('alcaldia', models.CharField(max_length=255, verbose_name='Alcaldia')),
                ('codigoPostal', models.CharField(max_length=10, verbose_name='Código Postal')),
                ('colonia', models.CharField(max_length=255, verbose_name='Colonia')),
                ('calle', models.CharField(max_length=255, verbose_name='Calle')),
                ('numero', models.PositiveIntegerField(verbose_name='Número')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo')),
                ('horaApertura', models.TimeField(verbose_name='Hora de Apertura')),
                ('horaCierre', models.TimeField(verbose_name='Hora de Cierre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sucursales', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('lastUpdate', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supervisor')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['id'],
            },
        ),
    ]