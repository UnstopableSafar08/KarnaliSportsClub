# Generated by Django 3.0.5 on 2022-08-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0009_imggall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslider',
            name='ImagePub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='imageslider',
            name='Image_Desc',
            field=models.TextField(default='Image Description here', max_length=800),
        ),
        migrations.AlterField(
            model_name='imageslider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='imggall',
            name='altTxt',
            field=models.CharField(default='Image Alt Text...', max_length=50),
        ),
        migrations.AlterField(
            model_name='imggall',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]