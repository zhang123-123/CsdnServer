# Generated by Django 2.0 on 2019-10-23 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0002_auto_20191023_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csdnblog',
            old_name='blog',
            new_name='blog_info',
        ),
    ]
