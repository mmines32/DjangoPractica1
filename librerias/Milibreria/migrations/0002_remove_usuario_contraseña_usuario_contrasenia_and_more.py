# Generated by Django 5.0.6 on 2024-06-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Milibreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.AddField(
            model_name='usuario',
            name='contrasenia',
            field=models.CharField(default='default_password', unique=True, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.IntegerField(unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(unique=True, verbose_name='Teléfono'),
        ),
    ]
