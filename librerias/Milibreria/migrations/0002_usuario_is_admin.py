# Generated by Django 5.0.6 on 2024-06-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Milibreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
