# Generated by Django 3.0.5 on 2022-08-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0021_auto_20220818_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='ksc/blogImage'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='KSC', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostDesc1',
            field=models.TextField(default='Enter Blog Content Here', max_length=2000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostH1',
            field=models.CharField(default='Enter Blog Title Here', max_length=150),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostH2',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostH3',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostImg1',
            field=models.ImageField(default='', upload_to='ksc/blogImage'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostImg2',
            field=models.ImageField(default='', upload_to='ksc/blogImage'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogPostImg3',
            field=models.ImageField(default='', upload_to='ksc/blogImage'),
        ),
    ]
