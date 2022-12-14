# Generated by Django 4.1.3 on 2022-11-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=128)),
                ('descripcion', models.CharField(default='', max_length=96)),
                ('fechaCreacion', models.CharField(default='', max_length=32)),
                ('fechaEntrega', models.CharField(default='', max_length=32)),
                ('usuarioDesignado', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=64)),
                ('apellido', models.CharField(default='', max_length=64)),
                ('codigo', models.CharField(default='', max_length=64)),
                ('contraseña', models.CharField(default='', max_length=64)),
            ],
        ),
    ]
