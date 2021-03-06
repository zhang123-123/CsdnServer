# Generated by Django 2.0 on 2019-10-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0007_auto_20191023_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZanCsdnBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='点赞人')),
                ('blog_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='博客id')),
                ('zan_status', models.BooleanField(default=False, verbose_name='点赞状态')),
            ],
            options={
                'verbose_name': '点赞状态表',
                'verbose_name_plural': '点赞状态表',
                'db_table': 'zancsdnblog',
            },
        ),
    ]
