# Generated by Django 4.0.4 on 2022-12-23 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_taller_nomtaller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taller',
            old_name='fechaTermnino',
            new_name='fechaTermino',
        ),
    ]
