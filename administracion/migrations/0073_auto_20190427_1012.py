# Generated by Django 2.0.10 on 2019-04-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0072_auto_20190326_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes')], default='Lunes', max_length=100)),
                ('Seccion', models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=7)),
            ],
        ),
        migrations.AlterModelOptions(
            name='asignacion_materia',
            options={'ordering': ['Grado']},
        ),
        migrations.AddField(
            model_name='horarioexamen',
            name='asignacion_materias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.Asignacion_Materia'),
        ),
        migrations.AddField(
            model_name='horarioexamen',
            name='horas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.horas'),
        ),
        migrations.AlterUniqueTogether(
            name='horarioexamen',
            unique_together={('asignacion_materias', 'dia', 'horas')},
        ),
    ]
