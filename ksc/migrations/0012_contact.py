# Generated by Django 3.0.5 on 2022-08-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0011_auto_20220805_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
