# Generated by Django 4.1 on 2022-09-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0024_remove_blogpost_blogpostdesc1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpost',
            name='event_post_desc',
            field=models.TextField(default='Enter Event Heading1 here', max_length=1000),
        ),
    ]
