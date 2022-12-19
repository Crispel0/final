# Generated by Django 4.1.3 on 2022-12-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0005_alter_tipoactivo_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='herramienta_cloud',
            field=models.CharField(choices=[('0', 'google drive'), ('1', 'one drive'), ('2', 'dropbox'), ('3', 'amazon cloud'), ('4', 'No instalado')], max_length=1, verbose_name='Herramienta Cloud'),
        ),
        migrations.AlterField(
            model_name='software',
            name='ofimatica',
            field=models.CharField(choices=[('0', 'Microsoft office'), ('1', 'Libre office'), ('2', 'Open office'), ('3', 'No instalado')], max_length=1, verbose_name='Ofimatica'),
        ),
        migrations.AlterField(
            model_name='software',
            name='version_ofimatica',
            field=models.CharField(choices=[('0', '2007'), ('1', '2010'), ('2', '2013'), ('3', '2016'), ('4', '2019'), ('5', '365'), ('6', '7.3.5'), ('7', '7.3.4'), ('8', '7.3.3'), ('9', '7.3.2'), ('10', '7.3.1'), ('11', '4.1.3'), ('12', '4.1.2'), ('13', '4.1.1'), ('14', '4.1.0'), ('15', '4.0.0'), ('16', 'No instalado')], max_length=3, verbose_name='Versión ofimatica'),
        ),
    ]
