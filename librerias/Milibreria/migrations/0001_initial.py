# Generated by Django 5.0.6 on 2024-06-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Precio')),
                ('imagen', models.CharField(max_length=100, null=True, verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=8, unique=True, verbose_name='DNI')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=20, unique=True, verbose_name='Teléfono')),
                ('password', models.CharField(default='', max_length=100, verbose_name='Contraseña')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
