# Generated by Django 3.0.5 on 2022-08-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0018_auto_20220816_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=130, unique=True),
        ),
    ]
