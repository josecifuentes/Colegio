# Generated by Django 2.0.9 on 2018-11-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_auto_20181103_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Inactivo', max_length=20),
        ),
    ]
