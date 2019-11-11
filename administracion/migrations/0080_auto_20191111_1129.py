# Generated by Django 2.0.10 on 2019-11-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0079_auto_20191108_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examene',
            name='Estado_Idioma',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reprobado', 'Reprobado'), ('Aprobado', 'Aprobado'), ('Nivelacion', 'Nivelacion')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='examene',
            name='Estado_Ingles',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reprobado', 'Reprobado'), ('Aprobado', 'Aprobado'), ('Nivelacion', 'Nivelacion')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='examene',
            name='Estado_Matematicas',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reprobado', 'Reprobado'), ('Aprobado', 'Aprobado'), ('Nivelacion', 'Nivelacion')], default='Pendiente', max_length=20),
        ),
    ]
