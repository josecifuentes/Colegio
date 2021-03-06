# Generated by Django 2.0.9 on 2019-01-10 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0049_auto_20190109_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividade',
            name='Grado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.Grado'),
        ),
        migrations.AlterField(
            model_name='actividade',
            name='Grupo',
            field=models.CharField(choices=[('estudiantes', 'Estudiantes'), ('estu-preprimaria', 'Estudiantes Pre-Primaria'), ('estu-primaria', 'Estudiantes Primaria'), ('estu-basico', 'Estudiantes Basico'), ('estu-bach', 'Estudiantes Bachillerato'), ('prof-preprimaria', 'Profesores Pre-Primaria'), ('prof-primaria', 'Profesores Primaria'), ('prof-basico', 'Profesores Basico'), ('profbach', 'Profesores Bachillerato'), ('todos', 'Todos')], default='Todos', max_length=30),
        ),
    ]
