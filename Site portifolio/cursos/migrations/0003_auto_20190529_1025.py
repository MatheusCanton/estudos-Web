# Generated by Django 2.2.1 on 2019-05-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20190523_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='carga_horaria',
        ),
        migrations.AddField(
            model_name='curso',
            name='coordenador',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='ementa',
            field=models.TextField(blank=True, null=True),
        ),
    ]