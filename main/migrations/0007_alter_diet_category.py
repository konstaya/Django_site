# Generated by Django 3.2.11 on 2022-01-15 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220115_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diets', to='main.category'),
        ),
    ]