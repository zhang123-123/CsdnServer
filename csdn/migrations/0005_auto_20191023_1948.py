# Generated by Django 2.0 on 2019-10-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0004_auto_20191023_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csdnblog',
            name='blog_time',
            field=models.TimeField(blank=True, null=True, verbose_name='博客发布日期'),
        ),
    ]
