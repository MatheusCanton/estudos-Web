# Generated by Django 2.2.1 on 2019-05-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='sigla',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
