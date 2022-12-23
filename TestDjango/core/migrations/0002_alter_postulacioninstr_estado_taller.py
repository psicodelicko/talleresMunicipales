# Generated by Django 4.0.4 on 2022-12-23 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacioninstr',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=50, verbose_name='estado de postulante'),
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('idTaller', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de taller')),
                ('descripcionTaller', models.CharField(max_length=50, verbose_name='Descripcion de taller')),
                ('sala', models.IntegerField(verbose_name='Sala de taller')),
                ('fechaInicio', models.CharField(max_length=50, verbose_name='Fecha inicio')),
                ('fechaTermnino', models.CharField(max_length=50, verbose_name='Fecha termino')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
