# Generated by Django 4.2.6 on 2023-10-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursoasignacion', '0004_alter_curso_catedratico_asignado_alter_curso_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='catedratico_asignado',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='cursoasignacion.catedratico'),
        ),
    ]
