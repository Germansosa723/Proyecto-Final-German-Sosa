# Generated by Django 4.1.3 on 2023-04-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGym', '0002_rutina_publicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutina',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='rutinas'),
        ),
    ]