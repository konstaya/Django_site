# Generated by Django 3.2.11 on 2022-01-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='type',
            field=models.BooleanField(default=True, verbose_name='Тип'),
        ),
    ]