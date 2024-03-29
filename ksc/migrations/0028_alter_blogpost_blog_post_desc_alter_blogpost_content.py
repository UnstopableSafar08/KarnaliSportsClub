# Generated by Django 4.1 on 2022-09-06 11:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ksc', '0027_rename_blogposth1_blogpost_blogpostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_post_desc',
            field=models.TextField(default="Blog Post's Desc only show in Blog page, It does not shown in Blog post View page", max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
