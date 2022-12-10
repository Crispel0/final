# Generated by Django 4.1.3 on 2022-12-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=4, unique=True, verbose_name='Tipo de Documento'),
        ),
    ]