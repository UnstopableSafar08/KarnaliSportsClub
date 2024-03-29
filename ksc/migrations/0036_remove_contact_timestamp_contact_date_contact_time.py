# Generated by Django 4.1 on 2022-09-16 06:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0035_remove_contact_date_remove_contact_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
