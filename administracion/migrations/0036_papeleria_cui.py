# Generated by Django 2.0.9 on 2018-11-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0035_examene_fechaingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='papeleria',
            name='Cui',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
