# Generated by Django 2.0.9 on 2018-11-04 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0012_auto_20181104_1632'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pago',
            unique_together={('Alumno', 'Tipo_Pago')},
        ),
    ]
