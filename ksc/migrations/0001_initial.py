# Generated by Django 3.2.5 on 2022-07-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img_Name', models.CharField(max_length=80)),
                ('Img_Desc', models.CharField(max_length=800)),
                ('ImgPub_date', models.DateField()),
            ],
        ),
    ]