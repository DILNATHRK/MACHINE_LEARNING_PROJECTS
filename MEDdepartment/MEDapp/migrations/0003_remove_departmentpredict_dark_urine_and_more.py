# Generated by Django 4.1.1 on 2022-12-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MEDapp', '0002_alter_departmentpredict_itching_skin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentpredict',
            name='dark_urine',
        ),
        migrations.RemoveField(
            model_name='departmentpredict',
            name='itching_skin',
        ),
    ]
