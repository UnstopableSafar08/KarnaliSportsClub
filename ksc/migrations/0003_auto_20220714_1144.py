# Generated by Django 3.2.5 on 2022-07-14 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0002_auto_20220714_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageslider',
            old_name='Imgage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='imageslider',
            old_name='ImgagePub_date',
            new_name='ImagePub_date',
        ),
        migrations.RenameField(
            model_name='imageslider',
            old_name='Imgage_Desc',
            new_name='Image_Desc',
        ),
        migrations.RenameField(
            model_name='imageslider',
            old_name='Imgage_Name',
            new_name='Image_Name',
        ),
    ]
