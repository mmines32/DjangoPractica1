# Generated by Django 5.0.6 on 2024-07-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Milibreria', '0002_usuario_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.URLField(max_length=100, null=True, verbose_name='Imagen'),
        ),
    ]