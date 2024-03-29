# Generated by Django 4.1 on 2022-09-06 11:28

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0028_alter_blogpost_blog_post_desc_alter_blogpost_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='blogPostImg1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='blogPostImg2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='blogPostImg3',
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='eventImg1',
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='eventImg2',
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='eventImg3',
        ),
        migrations.AddField(
            model_name='eventpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='ksc/blogImage'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='eventpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
