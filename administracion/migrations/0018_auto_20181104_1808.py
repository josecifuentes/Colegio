# Generated by Django 2.0.9 on 2018-11-05 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0017_personal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion_Materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Grado')),
                ('Materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Materia')),
            ],
        ),
        migrations.RemoveField(
            model_name='grados_materias',
            name='Grado',
        ),
        migrations.RemoveField(
            model_name='grados_materias',
            name='Materia',
        ),
        migrations.AlterField(
            model_name='personal',
            name='Direccion',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Lugar_Nacimiento',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Grados_Materias',
        ),
        migrations.AddField(
            model_name='asignacion_materias',
            name='Personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Personal'),
        ),
    ]
