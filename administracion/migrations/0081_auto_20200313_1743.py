# Generated by Django 2.0.10 on 2020-03-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0080_auto_20191111_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='estados_materia',
            name='fechaingreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estados_materia',
            name='Estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('No Aprobado', 'No Aprobado'), ('Aprobado', 'Aprobado')], default='No Aprobado', max_length=20),
        ),
    ]
