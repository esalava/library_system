# Generated by Django 5.0 on 2023-12-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_libro_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateTimeField(null=True),
        ),
    ]
