# Generated by Django 4.1.3 on 2023-03-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_rutina', models.CharField(max_length=30)),
                ('tipo_de_rutina', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=120)),
                ('creado_el', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
