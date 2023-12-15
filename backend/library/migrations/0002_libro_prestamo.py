# Generated by Django 5.0 on 2023-12-12 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=256)),
                ('cantidad_disponible', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_fin', models.DateTimeField()),
                ('fecha_devolucion', models.DateTimeField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.user')),
            ],
        ),
    ]