# Generated by Django 3.0.5 on 2022-08-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0010_auto_20220804_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslider',
            name='Image_Desc',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='imggall',
            name='altTxt',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='date',
            field=models.DateField(default=''),
        ),
    ]
