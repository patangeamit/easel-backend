# Generated by Django 5.1.6 on 2025-02-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='movement',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='media/artworks/'),
        ),
    ]
