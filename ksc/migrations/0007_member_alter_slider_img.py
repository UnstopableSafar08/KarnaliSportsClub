# Generated by Django 4.0.6 on 2022-07-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0006_alter_slider_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberName', models.CharField(max_length=50)),
                ('memberPosition', models.CharField(max_length=50)),
                ('memberImg', models.ImageField(default='', upload_to='ksc/images')),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(default='', upload_to='ksc/images'),
        ),
    ]