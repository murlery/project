# Generated by Django 5.1 on 2024-10-08 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoos', '0002_style_alter_tattoo_options_remove_tattoo_style_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoo',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tattoos.style'),
        ),
    ]