# Generated by Django 2.0 on 2019-10-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0014_auto_20191024_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='csdnblog',
            name='blog_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='博客类别id'),
        ),
    ]
