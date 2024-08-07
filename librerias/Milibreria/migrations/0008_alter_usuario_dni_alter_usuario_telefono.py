# Generated by Django 5.0.6 on 2024-07-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Milibreria', '0007_alter_usuario_dni_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.PositiveIntegerField(unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.PositiveIntegerField(unique=True, verbose_name='Teléfono'),
        ),
    ]
