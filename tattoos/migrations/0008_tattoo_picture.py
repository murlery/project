# Generated by Django 5.1 on 2024-11-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoos', '0007_tattoostudio_tattooartist_tattoostudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoo',
            name='picture',
            field=models.ImageField(null=True, upload_to='tattoos', verbose_name='Изображение'),
        ),
    ]
