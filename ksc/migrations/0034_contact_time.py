# Generated by Django 4.1 on 2022-09-16 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0033_remove_contact_timestamp_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
