# Generated by Django 4.2.7 on 2023-11-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangolibrarymgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=255),
        ),
    ]
