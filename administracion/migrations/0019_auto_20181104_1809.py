# Generated by Django 2.0.9 on 2018-11-05 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0018_auto_20181104_1808'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='asignacion_materias',
            unique_together={('Grado', 'Materia')},
        ),
    ]
