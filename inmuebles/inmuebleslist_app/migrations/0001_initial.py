# Generated by Django 5.1 on 2024-08-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=250)),
                ('pais', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.CharField(max_length=900)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
