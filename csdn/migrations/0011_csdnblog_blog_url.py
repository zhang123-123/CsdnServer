# Generated by Django 2.0 on 2019-10-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0010_auto_20191024_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='csdnblog',
            name='blog_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='博客原文链接'),
        ),
    ]