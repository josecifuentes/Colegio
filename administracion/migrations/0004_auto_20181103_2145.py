# Generated by Django 2.0.9 on 2018-11-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_auto_20181103_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grado',
            name='Nivel',
            field=models.CharField(choices=[('Pre-Primaria', 'Pre-Primaria'), ('Primaria', 'Primaria'), ('Basico', 'Basico'), ('Diversificado', 'Diversificado')], default='Pre-Primaria', max_length=100),
        ),
    ]
