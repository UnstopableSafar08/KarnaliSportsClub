# Generated by Django 3.0.5 on 2022-08-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0019_auto_20220817_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='slug',
            field=models.CharField(max_length=130, null=True),
        ),
    ]