# Generated by Django 2.0.9 on 2018-11-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0021_auto_20181104_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='No_Hijos',
            field=models.CharField(choices=[('sin', 'Sin Hijos'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('mas', 'Mas de 5...')], default='sin', max_length=20),
        ),
    ]
